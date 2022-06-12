from django.core.exceptions import ValidationError
from django.http import Http404
from django.urls import reverse


def next_or_home(request):
    if 'next' in request.GET:
        return request.GET['next']
    if 'next' in request.POST:
        return request.POST['next']
    return reverse('core:home')


def get_object_or_404(model, pk):
    try:
        return model.objects.get(pk=pk)
    except (ValidationError, model.DoesNotExist):
        raise Http404()
