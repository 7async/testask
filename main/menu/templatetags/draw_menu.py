from django import template
from menu.models import Menu, MenuItem
import pprint


register = template.Library()

@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, name):
    # graph-like structure to store menu data
    qs = MenuItem.objects.filter(menu__name=name)
    nodes = {item: [] for item in qs}
    for item in qs:
        if item.parent:
            nodes[item.parent].append(item)
    return {'items': nodes, 'context': context}

@register.inclusion_tag('menu/branch.html', takes_context=True)
def draw_branch(context, items, children):
    path = context.request.path.split('/')[1:]
    url = context.request.path
    return {'items': items, 'children': children, 'path': path, 'url': url}

@register.filter
def get_value(dictionary, key):
    return dictionary.get(key)