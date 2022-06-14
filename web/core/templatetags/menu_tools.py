from django import template

from core.menu import MENU, MenuItem

register = template.Library()


@register.inclusion_tag('widgets/menu.html', takes_context=True)
def menu(context, name):
    menu: MenuItem = MENU[name]
    return {
        'title': menu.as_title,
        'item': menu.as_item,
        'level': 1,
        'has_children': menu.has_children,
        'children': menu.get_children(context.request),
        'is_active': menu.is_active(context.request),
    }


@register.inclusion_tag('widgets/menu.html', takes_context=True)
def submenu(context, menu, level):
    return {
        'title': menu.as_title,
        'item': menu.as_item,
        'level': level + 1,
        'has_children': menu.has_children,
        'children': menu.get_children(context.request),
        'is_active': menu.is_active(context.request),
    }
