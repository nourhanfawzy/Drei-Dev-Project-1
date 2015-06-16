from django.views.generic import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from app1.models import Book, Library, Notification
from app1.forms import BookForm
from django.forms.models import modelformset_factory
from app1.views import PaginateMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, HttpResponseRedirect, render, HttpResponse
from django.db.models.signals import post_save
from django.dispatch import receiver


class BookCreate(View):
    """
    Creates a new book model.
    :author Nourhan Fawzy:
    :param CreateView:
    :return:
    """

    model = Book
    fields = ['name', 'year', 'about']
    BookFormSet = modelformset_factory(
            model=Book,
            fields=['name', 'year', 'about'], form=BookForm, extra=3)

    def get_context_data(self, **kwargs):
        context = super(BookCreate, self).get_context_data(**kwargs)
        context['library_id'] = self.request.user.library.all()[0].id
        if self.request.POST:
            context['book_form'] = self.BookFormSet(self.request.POST)
        else:
            context['book_form'] = self.BookFormSet()
        return context

    def post(self, args, **kwargs):
        library = Library.objects.get(id=self.kwargs['library_id'])
        formset = self.BookFormSet(
            self.request.POST)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.library = library
                instance.save()
        return HttpResponseRedirect(
            reverse(
                'book_list',
                kwargs={"library_id": self.request.user.library.all()[0].id}))

    def get(self, args, **kwargs):
        return render(
            self.request, "app1/book_form.html", {
                "book_form": self.BookFormSet(
                    queryset=Book.objects.none()),
                "library_id": self.request.user.library.all()[0].id
            })


class BookUpdate(UpdateView):
    """
    Updates a book model.
    :author Nourhan Fawzy:
    :param UpdateView:
    :return:
    """

    model = Book
    fields = ['name', 'year', 'about']
    template_name_suffix = '_update_form'

    # Try to use formset to update more than book at once


class BookDelete(DeleteView):
    """
    Deletes a book model.
    :author Nourhan Fawzy:
    :param DeleteView:
    :return:
    """

    model = Book

    def get_success_url(self):

        return reverse('book_list',
                       kwargs=
                       {'library_id': self.request.user.library.all()[0].id}
                       )


class MyBookListView(PaginateMixin, ListView):
    """
    Lists all books for a certain library.
    :author Nourhan Fawzy:
    :param PaginateMixin, ListView:
    :return:
    """

    model = Book

    def get_queryset(self):
        """
        Gets a queryset of books.
        :author Nourhan Fawzy:
        :param self:
        :return Books list for certain library:
        """

        return Book.objects.filter(library_id=self.kwargs['library_id'])

    def get_context_data(self, **kwargs):
        """
        Gets a list of books for a given library.
        :author Nourhan Fawzy:
        :param self, keyword arguments:
        :return context:
        """

        context = super(MyBookListView, self).get_context_data(**kwargs)
        library = get_object_or_404(Library, id=self.kwargs['library_id'])
        context['library'] = library
        return context


class MyBookDetailView(DetailView):
    """
    Shows details of a book model.
    :author Nourhan Fawzy:
    :param DetailView:
    :return:
    """

    model = Book

    def get_context_data(self, **kwargs):
        """
        Gets context details of a book model.
        :author Nourhan Fawzy:
        :param self, keyword arguments:
        :return context:
        """

        context = super(MyBookDetailView, self).get_context_data(**kwargs)
        return context


class LibrariesListView(PaginateMixin, ListView):
    """
    Lists all libraries available on the website.
    :author Nourhan Fawzy:
    :param PaginateMixin, ListView:
    :return:
    """

    model = Library

    def get_context_data(self, **kwargs):
        """
        Gets a list of all libraries in the database.
        :author Nourhan Fawzy:
        :param self, keyword arguments:
        :return context:
        """

        context = super(LibrariesListView, self).get_context_data(**kwargs)
        return context


class LibrariesDetailView(DetailView):
    """
    Shows details of a library model.
    :author Nourhan Fawzy:
    :param DetailView:
    :return:
    """

    model = Library

    def get_context_data(self, **kwargs):
        """
        Gets context details of a library model.
        :author Nourhan Fawzy:
        :param self, keyword arguments:
        :return context:
        """

        context = super(LibrariesDetailView, self).get_context_data(**kwargs)
        return context


@receiver(post_save, sender=Book)
def create_notification(sender, **kwargs):
    """
    A function that creates a new notification once a new
    book is created and is sent to all users except the user
    that has just created the book.
    :author Nourhan Fawzy:
    :param sender, keyword arguments:
    :return:
    """

    if kwargs.get('created', False):
        book = kwargs.get('instance')
        library = Library.objects.get(id=book.library.id)
        signed_in_user = User.objects.get(id=library.created_by.id)
        users = User.objects.exclude(id=signed_in_user.id)

        for user in users:
            Notification.objects.create(book_name=book.name,
            library=library, notified_user=user)


class NotificationListView(PaginateMixin, ListView):
    """
    Lists all notifications when a new book is created.
    :author Nourhan Fawzy:
    :param PaginateMixin, ListView:
    :return:
    """

    model = Notification

    def get_context_data(self, **kwargs):
        """
        Gets a list of notifications for a given user.
        :author Nourhan Fawzy:
        :param self, keyword arguments:
        :return context:
        """

        context = super(NotificationListView, self).get_context_data(**kwargs)

        unread = Notification.objects.filter(
            status=0, notified_user=self.request.user.id)
        read = Notification.objects.filter(
            status=1, notified_user=self.request.user.id)

        for notification in unread:
            notification.status = 1
            notification.save()

        context['read'] = read
        context['unread'] = unread

        return context
