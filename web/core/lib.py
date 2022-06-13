import markdown as md
import bleach

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


def translate_all(value):
    filters = [
        translate_markdown,
        filter_html,
    ]

    result = value
    for filter in filters:
        result = filter(result)

    return result


def translate_markdown(value):
    return md.markdown(value, extensions=[
        'markdown.extensions.fenced_code',
        'markdown.extensions.admonition',
        'markdown.extensions.sane_lists',
    ])


def filter_html(value):
    return bleach.clean(value,
                        tags=['h2', 'h3', 'h4', 'h5',
                              'a', 'p', 'em', 'i', 'b', 'strong', 'abbr', 'acronym',
                              'ul', 'ol', 'li',
                              'span', 'div', 'code',
                              ],
                        attributes={
                            '*': ['class', 'title', 'style'],
                            'a': ['href', 'rel'],
                            'img': ['src', 'alt'],
                        })
