from app1.models import Library
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from app1.forms import UserForm, LibraryForm
from django.core.urlresolvers import reverse
# Create your views here.


def home(request):
    return render_to_response(
        'home.html', {}, context_instance=RequestContext(request))


def user_account(request, u_id):
    user = User.objects.get(id=u_id)
    user_library = Library.objects.get(created_by=user)

    if request.POST:
        user.first_name = request.POST['firstname']
        user.save()

        user.last_name = request.POST['lastname']
        user.save()

        user.email = request.POST['email']
        user.save()

        user.set_password = request.POST['newpassword']
        user.save()

        user_library.name = request.POST['library_name']
        user_library.save()

        user_library.location = request.POST['library_location']
        user_library.save()

    return render_to_response(
        'myaccount.html', {'user': user, 'user_library': user_library},
        context_instance=RequestContext(request))


def user_edit_account(request, u_id):
    user = User.objects.get(id=u_id)
    user_library = Library.objects.get(created_by=user)

    return render_to_response(
        'editaccount.html', {'user': user, 'user_library': user_library},
        context_instance=RequestContext(request))


def user_signup(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        library_form = LibraryForm(data=request.POST)

        if user_form.is_valid() and library_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            user_library = library_form.save(commit=False)
            user_library.created_by = user
            user_library.save()
            registered = True
        else:
            print user_form.errors, library_form.errors

    else:
        user_form = UserForm()
        library_form = LibraryForm()
        return render_to_response(
            'signup.html',
            {'user_form': user_form, 'library_form': library_form},
            context_instance=RequestContext(request))

    return render_to_response(
                'home.html', {'user': user, 'user_library': user_library,
                'registered': registered},
                context_instance=RequestContext(request))


def user_signin(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                user_library = Library.objects.get(created_by=user)
                registered = True
                return render_to_response(
                    'home.html',
                    {'user': user, 'user_library': user_library,
                    'registered': registered}, context)
            else:
                return HttpResponse("Your financeweb account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('signin.html', {}, context)


@login_required
def user_signout(request):
    logout(request)
    url = reverse('home')
    return HttpResponseRedirect(url)
