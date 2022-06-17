from collections import defaultdict, OrderedDict

from django import template
from django.db.models import Q
from django.urls import reverse
from django.utils.translation import gettext as _

from core.menu import MenuItem
from crm.models import Reference

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


@register.inclusion_tag('crm/relations.html', takes_context=True)
def entity_relations(context, entity):
    structured_relations = OrderedDict()
    for type, reference in Reference.objects.collect_for(entity):
        structured_relations.setdefault(type, []).append(reference)

    return {
        'relations': structured_relations.items()
    }
