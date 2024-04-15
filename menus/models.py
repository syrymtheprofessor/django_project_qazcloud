# models.py
from django.db import models
from django_extensions.db.fields import AutoSlugField

from wagtail.admin.panels import (FieldPanel, InlinePanel, PageChooserPanel)
from wagtail.models import Orderable, ClusterableModel
from modelcluster.fields import ParentalKey
from wagtail.snippets.models import register_snippet

from wagtail.contrib.modeladmin.options import (
   ModelAdmin,
   modeladmin_register,
)

class Footer(models.Model):
    pass

@register_snippet
class QazcloudMenu(models.Model):
    # о компании
    about_title = models.CharField(max_length=512, blank=True, null=True)
    about_context = models.CharField(max_length=512, blank=True, null=True)

    # карьера
    career_title = models.CharField(max_length=512, blank=True, null=True)
    career_context = models.CharField(max_length=512, blank=True, null=True)
    
    # Юр инфо
    law_info = models.CharField(max_length=512, blank=True, null=True)
    law_context = models.CharField(max_length=512, blank=True, null=True)
    law_address = models.CharField(max_length=512, blank=True, null=True)
    law_address_name = models.CharField(max_length=512, blank=True, null=True)
    law_address_address = models.CharField(max_length=512, blank=True, null=True)
    law_contract1 = models.CharField(max_length=512, blank=True, null=True)
    law_contract2 = models.CharField(max_length=512, blank=True, null=True)

    # Contacts
    address_title = models.CharField(max_length=512, blank=True, null=True)
    address_name1 = models.CharField(max_length=512, blank=True, null=True)
    address_address1 = models.CharField(max_length=512, blank=True, null=True)

    address_name2 = models.CharField(max_length=512, blank=True, null=True)
    address_address2 = models.CharField(max_length=512, blank=True, null=True)

    address_name3 = models.CharField(max_length=512, blank=True, null=True)
    address_address3 = models.CharField(max_length=512, blank=True, null=True)

    contacts_contacts_title = models.CharField(max_length=512, blank=True, null=True)
    contacts_tech_title = models.CharField(max_length=512, blank=True, null=True)
    contacts_tech_number = models.CharField(max_length=512, blank=True, null=True)
    contacts_sales_title = models.CharField(max_length=512, blank=True, null=True)
    contacts_sales_number = models.CharField(max_length=512, blank=True, null=True)
    

    # Press
    press_mail = models.CharField(max_length=512, blank=True, null=True)
    press_context = models.CharField(max_length=512, blank=True, null=True)
    logo1 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    logo2 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    def __str__(self): 
        return "Qazcloud меню"

# fill the panels, with labels and fields, in russian
panels = [
    FieldPanel('about_title', heading="О компании, заголовок"),
    FieldPanel('about_context', heading="О компании, контекст"),
    FieldPanel('career_title', heading="О компании, заголовок"),
    FieldPanel('career_context', heading="О компании, контекст"),
    FieldPanel('law_info', heading="Юр инфо, заголовок"),
    FieldPanel('law_context', heading="Юр инфо, контекст"),
    FieldPanel('law_address', heading="Юр инфо, заголовок адреса"),
    FieldPanel('law_address_name', heading="Юр инфо, название филиала"),
    FieldPanel('law_address_address', heading="Юр инфо, адрес"),
    FieldPanel('law_contract1', heading="Юр инфо, контракт"),
    FieldPanel('law_contract2', heading="Юр инфо, контракт"),
    FieldPanel('address_title', heading="Контакты, блок адрес заголовок"),
    FieldPanel('address_name1', heading="Контакты, название филиала"),
    FieldPanel('address_address1', heading="Контакты, адрес"),
    FieldPanel('address_name2', heading="Контакты, название филиала"),
    FieldPanel('address_address2', heading="Контакты, адрес"),
    FieldPanel('address_name3', heading="Контакты, название филиала"),
    FieldPanel('address_address3', heading="Контакты, адрес"),
    FieldPanel('contacts_contacts_title', heading="Контакты, заголовок"),
    FieldPanel('contacts_tech_title', heading="Контакты, отдел техподдержки"),
    FieldPanel('contacts_tech_number', heading="Контакты, номер техподдержки"),
    FieldPanel('contacts_sales_title', heading="Контакты-отдел-продаж"),
    FieldPanel('contacts_sales_number', heading="Контакты-номер продаж"),
    FieldPanel('press_mail', heading="Пресс-служба-почта"),
    FieldPanel('press_context', heading="Пресс-служба-контекст"),
    FieldPanel('logo1', heading="Логотип 1"),
    FieldPanel('logo2', heading="Логотип 2"),
]

@register_snippet
class MenuItem(ClusterableModel):
    link_title = models.CharField(max_length=100, blank=True, null=True)
    slug = AutoSlugField(populate_from="link_title", editable=True)
    priority = models.IntegerField(blank=True, null=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.CASCADE
    )
    has_submenu = models.BooleanField(default=False, blank=True)

    panels = [
        FieldPanel('link_title'),
        FieldPanel('slug'),
        FieldPanel('priority'),
        PageChooserPanel('link_page'),
        FieldPanel('has_submenu'),
        InlinePanel('submenu_items', label="Submenu Items"),
    ]
    
    def __str__(self): 
        return self.link_title
  
class SubMenuItem(ClusterableModel, Orderable):
    parent = ParentalKey(MenuItem, related_name='submenu_items', on_delete=models.CASCADE, null=True, blank=True)
    subitem_title = models.CharField(max_length=50, blank=True, null=True)

    panels = [
        FieldPanel('subitem_title'),
        InlinePanel('dropdown_items', label="Dropdown Items"),
    ]

class DropdownContext(Orderable):
    parent = ParentalKey(SubMenuItem, related_name='dropdown_items', on_delete=models.CASCADE, null=True, blank=False)
    dropdown_header = models.CharField(max_length=250, blank=True, null=True)
    dropdown_context = models.TextField()
    dropdown_icon =  models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.CASCADE
    )
    panels = [
        FieldPanel('dropdown_header'),
        FieldPanel('dropdown_context'),
        FieldPanel('dropdown_icon'),
        PageChooserPanel('link_page')
    ]
