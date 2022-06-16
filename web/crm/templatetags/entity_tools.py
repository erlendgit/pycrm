from django import template
from django.urls import reverse
from django.utils.translation import gettext as _

from core.menu import MenuItem

register = template.Library()


@register.inclusion_tag('widgets/menu.html', takes_context=True)
def entity_menu(context, entity_id):
    menu = MenuItem(title=_("Entity menu"))
    return {
        'title': menu.as_title,
        'item': menu.as_item,
        'level': 1,
        'has_children': True,
        'children': [MenuItem(_('Update'), reverse("crm:update", args=[entity_id])),
                     MenuItem(_('Add relation'), reverse("crm:relate", args=[entity_id])),
                     MenuItem(_('Delete'), reverse("crm:delete", args=[entity_id]))],
        'is_active': menu.is_active(context.request),
    }
