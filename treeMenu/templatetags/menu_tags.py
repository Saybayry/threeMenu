from django.shortcuts import render
from django import template
from django.template.loader import render_to_string
from ..models import Menu, MenuItem
from django.http import QueryDict
register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context,name_menu, *args, **kwargs):
    request = context['request']
    url = request.build_absolute_uri()
    path_url = url.split('?')[0]
    query_string = url.split('?')[1] if len(url.split('?')) >= 2 else ''
    query_dict = QueryDict(query_string, mutable=True)
    menu_params = f'menu__{name_menu}'

    if menu_params in request.GET:
        select_menu_item = int( request.GET[menu_params])
    else:
        select_menu_item = None

    if menu_params in query_dict:
        del query_dict[menu_params]
    new_query_string = query_dict.urlencode()
    menu_items = MenuItem.objects.filter(parent_menu__name=name_menu)
    menu_items = list(menu_items)
    root_menu = list(filter(lambda x: x.parent == None  , menu_items))
    select_items = []
    child_items = []
    select_item = next(filter(lambda x: x.pk ==select_menu_item,menu_items), None)
    def select_menu(list_items, select_item):
        """this function collects the branch to the root
        """
        for item in list_items:
            if select_item.parent == None:
                return None
            if item == select_item.parent :
                select_items.append(item)
                select_menu(list_items, item)
    if select_item != None:

        select_items = []
        select_items.append(select_item)
        from pprint import pprint

        select_menu(menu_items, select_item)

        for el in menu_items:
            if el in select_items:
                pass
            else:
                if el.parent in select_items:
                    child_items.append(el)
                pass

    out_items = sorted((child_items + select_items), key=lambda x: -x.pk, reverse=True)


    context = {'filter_menu': root_menu,
               'menu_items': out_items,
               'select_menu_item': select_menu_item,
               'path_url': path_url,
               'other_params': new_query_string,
               'menu_params':menu_params
               }

    rendered_template = render_to_string('menu.html', context)
    return rendered_template




















