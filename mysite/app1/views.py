from django.shortcuts import render_to_response, RequestContext


def home(request):
    """
    A function used to redirect to homepage.
    :author Nourhan Fawzy:
    :param request:
    :return render_to_response:
    """
    return render_to_response(
        'home.html', {}, context_instance=RequestContext(request))


class PaginateMixin(object):
    """
    A Mixin used to paginate any object_list.
    :author Nourhan Fawzy:
    :param object:
    :return:
    """

    paginate_by = 3
