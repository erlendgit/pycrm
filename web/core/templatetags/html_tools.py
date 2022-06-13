from django import template

from django.utils.safestring import mark_safe

from core.lib import translate_all

register = template.Library()


@register.inclusion_tag('widgets/intended_markup.html')
def markdown(value):
    return {
        'content': mark_safe(translate_all(value))
    }
