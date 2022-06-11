from django.urls import reverse


def default_url(request):
    if 'origin' in request.GET:
        return request.GET['origin']
    return reverse('core:home')
