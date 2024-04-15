# templatetags/menu_tags.py
from django import template
from menus.models import MenuItem, Footer, DropdownContext, SubMenuItem, QazcloudMenu

register = template.Library()

@register.inclusion_tag('menus/tags/menu_test.html', takes_context=True)
def menu(context):
    menuItems = MenuItem.objects.all().order_by('-priority')
    subMenu = SubMenuItem.objects.all()
    qazcloud_menu = QazcloudMenu.objects.all()

    menuDropdownContext = DropdownContext.objects.all()
    map = {}

    for i in menuItems:
        map[i] = {}
        for j in subMenu:
            if j.parent == i:
                map[i][j] = []

                for k in menuDropdownContext:
                    if k.parent == j:
                        map.get(i).get(j).append(k)
                temp = map[i][j]
                map[i][j] = [temp[f:f+3] for f in range(0, len(temp), 3)]
    return {
        'map': map,
        'request': context['request'],
        'qazcloud_menu': qazcloud_menu[0    ]
    }

@register.inclusion_tag('menus/tags/qazcloud_menu.html', takes_context=True)
def qazcloudmenu(context):
    menu = QazcloudMenu.objects.all()
    return {
        'menu': menu
    }

@register.inclusion_tag('menus/tags/footer.html', takes_context=True)
def footer(context):
    footer = Footer.objects.all()
    return {
        'footer': footer,
        'request': context['request'],
    }