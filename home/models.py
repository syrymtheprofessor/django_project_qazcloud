from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.models import Orderable, ClusterableModel
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

from blog.models import Article
from products.models import FAQBlock, HaveAnyQuestions, NewsList, VideoBlock

# About US

class AboutUsOurTeamItems(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    title = blocks.CharBlock(required=True)
    name = blocks.CharBlock(required=True)

class AboutUsOurTeam(blocks.StructBlock):
    mini_header = blocks.CharBlock(required=True)
    main_header = blocks.CharBlock(required=True)
    description = blocks.CharBlock(required=True)
    items = blocks.ListBlock(AboutUsOurTeamItems())
    class Meta:
        template = 'home/about_us/about_us_our_team.html'
        label = 'Наша Команда'

class AboutUsOffices(blocks.StructBlock):
    title = blocks.CharBlock(required=True)

    image1 = ImageChooserBlock(required=False)
    header1 = blocks.CharBlock(required=True)
    description1 = blocks.CharBlock(required=True)

    image2 = ImageChooserBlock(required=False)
    header2 = blocks.CharBlock(required=True)
    description2 = blocks.CharBlock(required=True)

    image3 = ImageChooserBlock(required=False)
    header3 = blocks.CharBlock(required=True)
    description3 = blocks.CharBlock(required=True)

    class Meta:
        template = 'home/about_us/about_us_offices.html'
        label = 'Наши офисы'

class AboutUsDevelopWithUsItems(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    subtitle = blocks.CharBlock(required=True)

class AboutUsDevelopWithUsIcons(blocks.StructBlock):
    icon = ImageChooserBlock(required=False)

class AboutUsDevelopWithUs(blocks.StructBlock):
    main_header = blocks.CharBlock(required=True)
    elipse = ImageChooserBlock(required=False)
    items = blocks.ListBlock(AboutUsDevelopWithUsItems())
    icons = blocks.ListBlock(AboutUsDevelopWithUsIcons())

    class Meta:
        template = 'home/about_us/about_us_develop.html'

class AboutUsSecondaryBlock(blocks.StructBlock):
    main_header = blocks.CharBlock(required=True)
    main_description = blocks.CharBlock(required=True)
    secondary_description = blocks.CharBlock(required=False)

    class Meta:
        template = 'home/about_us/about_us_secondary.html'

class AboutUsHero(blocks.StructBlock):
    main_header = blocks.CharBlock(required=True)
    secondary_header = blocks.CharBlock(required=True)
    description = blocks.CharBlock(required=True)
    image = ImageChooserBlock(required=True)

    class Meta:
        template = 'home/about_us/about_us_hero.html'
        label = 'Главный блок'

class AboutUs(Page):
    body = StreamField([
        ('about_us_hero', AboutUsHero()),
        ('secondary_header', AboutUsSecondaryBlock()),
        ('develop_with_us', AboutUsDevelopWithUs()),
        ('offices', AboutUsOffices()),
        ('oue_team', AboutUsOurTeam()),
        ('have_any_questions', HaveAnyQuestions()),
        ('video_block', VideoBlock()),

    ], null=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

class RootPageFeatureServicesIconChoose(blocks.StructBlock):
    icon = ImageChooserBlock(required=True)
    title = blocks.CharBlock(required=True)
    class Meta:
        label = "Добавление иконок с текстом"

class RootPageFeatureServicesSlider(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    class Meta:
        label = "Добавление фона для ползунка"

class RootPageFeatureServices(blocks.StructBlock):
    main_header = blocks.CharBlock(required=True, label='')
    icons = blocks.ListBlock(RootPageFeatureServicesIconChoose(),required=True, label='Иконки с текстом')
    slider = blocks.ListBlock(RootPageFeatureServicesSlider(),required=True, label='Ползунок')
    class Meta:
        template = 'home/blocks/feature_services.html'
        label = 'Блок "Услуги"'

class RootPageHeroBlock(blocks.StructBlock):
    main_header = blocks.CharBlock(required=True, label='Заголовок')
    subtitle_header = blocks.CharBlock(required=True, label='Текст')
    btn_text = blocks.CharBlock(required=False, label='Кнопка')
    hero_image = ImageChooserBlock(required=True, label='Изображение')
    class Meta:
        template = 'home/blocks/hero_block.html'
        label = 'Блок "Главный блок"'

class RootPageClientsImages(blocks.StructBlock):
    image = ImageChooserBlock(required=True)
    class Meta:
        label = 'Добавление клиентов'

class RootPageClients(blocks.StructBlock):
    title  = blocks.CharBlock(required=True)
    images = blocks.ListBlock(RootPageClientsImages())
    class Meta:
        template = 'home/blocks/clients.html'
        label = 'Блок "Клиенты"'

class RootPageProductsItem(blocks.StructBlock):
    name = blocks.CharBlock(required=True, label='Название')
    description = blocks.CharBlock(required=True, label='Описание')
    image = ImageChooserBlock(required=True, label='Иконка')
    link_page = blocks.PageChooserBlock(required=False, label='Ссылка на страницу')

class RootPageProducts(blocks.StructBlock):
    title = blocks.CharBlock(required=True, label='Заголовок')
    items = blocks.ListBlock(RootPageProductsItem(), label='Список продуктов')

    class Meta:
        template = 'home/blocks/products.html'
        label = 'Блок "Продукты"'

class RootPageWhyChooseUsItems(blocks.StructBlock):
    icon = ImageChooserBlock(required=True)
    title = blocks.CharBlock(required=True)
    description = blocks.CharBlock(required=True)
    class Meta:
        label = 'Добавление иконок с текстом'

class RootPageWhyChooseUs(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    items = blocks.ListBlock(RootPageWhyChooseUsItems())
    class Meta:
        template = 'home/blocks/why_choose_us.html'
        label = 'Блок "Почему мы"'

class RootPage(Page):
    body = StreamField([
        ('root_page_hero_block', RootPageHeroBlock()),
        ('root_page_products', RootPageProducts()),
        ('root_page_clients', RootPageClients()),
        ('root_page_why_choose_us', RootPageWhyChooseUs()),
        ('root_page_feature_services', RootPageFeatureServices()),
        ('news_list', NewsList()),
        ('faq', FAQBlock()),
        ('have_any_questions', HaveAnyQuestions()),
        ('video_block', VideoBlock()),
    ], null=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]