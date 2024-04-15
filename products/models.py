from django.db import models

from wagtail import blocks
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Orderable, ClusterableModel
# Create your models here.

from blog.models import Article

from django import template

register = template.Library()

class FAQItemBlock(blocks.StructBlock):
    question = blocks.CharBlock(required=True)
    answer = blocks.TextBlock(required=True)

    class Meta:
        icon = 'question'  # the icon that will appear in the admin
        label = 'FAQ Item'

class FAQBlock(blocks.StructBlock):
    header = blocks.CharBlock(required=True)
    subtitle = blocks.CharBlock(required=False)
    items = blocks.ListBlock(FAQItemBlock())
    class Meta:
        template = 'products/blocks/reserve_copy/faq.html'  # specify your own template here
        label = 'FAQ'

class HaveAnyQuestions(blocks.StructBlock):
    header = blocks.CharBlock(required=True)
    subtitle = blocks.CharBlock(required=True)
    button_subtitle = blocks.CharBlock(required=True)
    image = ImageChooserBlock()
    class Meta:
        template = 'products/blocks/reserve_copy/have_any_questions.html'  # specify your own template here
        label = 'Блок "Вопросы"'

class VideoBlock(blocks.StructBlock):
    header = blocks.CharBlock(required=True)
    body = blocks.RichTextBlock(required=True)

    class Meta:
        template = 'products/blocks/reserve_copy/video_block.html'  # Укажите свой собственный шаблон здесь
        label = 'Блок "Заголовок+Контент"'

class HeroBlock(blocks.StructBlock):
    hero_title = blocks.CharBlock(required=True)
    hero_subtitle = blocks.CharBlock(required=True)
    hero_image = ImageChooserBlock()

    class Meta:
        template = 'products/blocks/reserve_copy/hero.html'  # specify your own template here
        label = 'Hero Part'

class ReserveCopyAboutProduct(blocks.StructBlock):
    little_header = blocks.CharBlock(required=True)
    main_header = blocks.CharBlock(required=True)
    paragraph1 = blocks.CharBlock(required=True)
    image = ImageChooserBlock()
    paragraph2 = blocks.CharBlock(required=True)
    paragraph3 = blocks.CharBlock(required=True)

    class Meta:
        template = 'products/blocks/reserve_copy/reserve_copy_about_product.html'  # specify your own template here
        icon = 'question'  # the icon that will appear in the admin
        label = 'ReserveCopyAboutProduct'

class AdvantagesItemBlock(blocks.StructBlock):
    icon = ImageChooserBlock()
    title = blocks.CharBlock(required=True)
    subtitle = blocks.CharBlock(required=True)
    

    class Meta:
        icon = 'advantages_items'
        label = 'Advantages_item'

class FloatingBlock(blocks.StructBlock):
    context = blocks.CharBlock(required=True)
    js_link = blocks.ListBlock(blocks.CharBlock(required=True))

    class Meta:
        template = 'products/blocks/reserve_copy/floating_block.html'
        label = 'Содержимое'

class Advantages(blocks.StructBlock):
    mini_header = blocks.CharBlock(required=True)
    header = blocks.CharBlock(required=True)
    items = blocks.ListBlock(AdvantagesItemBlock())
    paragraph = blocks.CharBlock(required=False)
    
    class Meta:
        template = 'products/blocks/reserve_copy/advantage.html'
        icon = 'advantages'
        label = 'Advantages'

class ServiceTableRowBlock(blocks.StructBlock):
    column1 = blocks.CharBlock(required=True)
    column2 = blocks.CharBlock(required=True)

    class Meta:
        icon = 'table'  # the icon that will appear in the admin
        label = 'Table Row'

class ReserveCopySERVICE(blocks.StructBlock):
    mini_header = blocks.CharBlock(required=True)
    header = blocks.CharBlock(required=True)
    table_rows = blocks.ListBlock(ServiceTableRowBlock())
    paragraph = blocks.CharBlock(required=True)
    class Meta:
        template = 'products/blocks/reserve_copy/reserve_copy_service.html'  # specify your own template here
        icon = 'table'  # the icon that will appear in the admin
        label = 'Table Row'

class ReserveCopy(Page):
    body = StreamField([
        ('faq', FAQBlock()),
        ('have_any_questions', HaveAnyQuestions()),
        ('hero', HeroBlock()),
        ('advantages', Advantages()),
        ('reserve_copy_about_product', ReserveCopyAboutProduct()),
        ('reserve_copy_service', ReserveCopySERVICE()),
        ('floating_block', FloatingBlock()),
        ('video_block', VideoBlock()),
    ], null=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

class NewsList(blocks.StructBlock):
    title = blocks.CharBlock(required=True, label='Заголовок')

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['news'] = Article.objects.all()
        return context

    class Meta:
        template = 'products/blocks/vmware_cloud/news_list.html'  # specify your own template here
        label = 'Блок "Новости"'

class VmwareCloudComparisonParagraphs(blocks.StructBlock):
    title_paragraph = blocks.CharBlock(required=True)
    context_paragraph = blocks.CharBlock(required=True)
    class Meta:
        icon = 'paragraph'  # the icon that will appear in the admin
        label = 'Paragraph'

class VmwareCloudComparison(blocks.StructBlock):
    little_header = blocks.CharBlock(required=True)
    main_header = blocks.CharBlock(required=True)
    paragraphs = blocks.ListBlock(VmwareCloudComparisonParagraphs())
    image = ImageChooserBlock()

    class Meta:
        template = 'products/blocks/vmware_cloud/vmware_cloud_comparison.html'

class VmwareCloudPeculiaritiesIcons(blocks.StructBlock):
    icon = ImageChooserBlock()
    icons_title = blocks.CharBlock(required=True)
    class Meta:
        icon = 'paragraph'  # the icon that will appear in the admin
        label = 'Paragraph'

class VmwareCloudPeculiarities(blocks.StructBlock):
    little_header = blocks.CharBlock(required=True)
    main_header = blocks.CharBlock(required=True)
    paragraph_header = blocks.CharBlock(required=True)
    paragraph_context = blocks.CharBlock(required=True)
    image = ImageChooserBlock()
    icons_header = blocks.CharBlock(required=True)
    icons = blocks.ListBlock(VmwareCloudPeculiaritiesIcons())

    class Meta:
        template = 'products/blocks/vmware_cloud/vmware_cloud_peculiarities.html'
        label = 'Peculiarities'

class VmwareTypeCloudContext(blocks.StructBlock):
    paragraph_header = blocks.CharBlock()
    paragraph_context = blocks.CharBlock()
    image = ImageChooserBlock()

    class Meta:
        icon = 'TypeCloud'  # the icon that will appear in the admin
        label = 'TypeCloud'

class VmwareTypeCloud(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    body = blocks.CharBlock(required=True)
    type_items = blocks.ListBlock(VmwareTypeCloudContext())

    class Meta:
        template = 'products/blocks/vmware_cloud/type_cloud.html'
        label = 'TypeCloud'

class VmwareTypeCloudBlackItems(blocks.StructBlock):
    paragraph_header = blocks.CharBlock()
    paragraph_context = blocks.CharBlock()
    image = ImageChooserBlock()

    class Meta:
        icon = 'TypeCloud'  # the icon that will appear in the admin
        label = 'TypeCloud'

class VmwareTypeCloudBlack(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    body = blocks.CharBlock(required=True)
    type_items = blocks.ListBlock(VmwareTypeCloudBlackItems())

    class Meta:
        template = 'products/blocks/vmware_cloud/type_cloud_black.html'
        label = 'TypeCloudBlack'

class VmwareCloud(Page):
    body = StreamField([
        ('hero', HeroBlock()),
        ('faq', FAQBlock()),
        ('floating_block', FloatingBlock()),
        ('video_block', VideoBlock()),

        ('advantages', Advantages()),   
        ('have_any_questions', HaveAnyQuestions()),
        ('news', NewsList()),
        ('vmware_cloud_comparison', VmwareCloudComparison()),
        ('vmware_cloud_peculiarities', VmwareCloudPeculiarities()),
        ('vmware_type', VmwareTypeCloud()),
        ('vmware_type_black', VmwareTypeCloudBlack()),

    ], null=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

class EquipmentPlacementIcons(blocks.StructBlock):
    icon = ImageChooserBlock()
    icons_title = blocks.CharBlock(required=True)
    class Meta:
        icon = 'Icons'  # the icon that will appear in the admin
        label = 'Icons'

class EquipmentPlacementWhereIsEquipment(blocks.StructBlock):
    little_header = blocks.CharBlock(required=True)
    main_header = blocks.CharBlock(required=True)
    paragraph = blocks.CharBlock(required=True)
    icons = blocks.ListBlock(EquipmentPlacementIcons())
    image = ImageChooserBlock()

    class Meta:
        template = 'products/blocks/equipment_placement/where_is_equipment.html'
        label = 'Where Is Equipment'

class EquipmentPlacementServiceImageContext(blocks.StructBlock):
    context = blocks.CharBlock(required=True)
    class Meta:
        label = 'Image Context'

class EquipmentPlacementService(blocks.StructBlock):
    little_header = blocks.CharBlock(required=True)
    main_header = blocks.CharBlock(required=True)
    paragraph = blocks.CharBlock(required=True)
    image_context = blocks.ListBlock(EquipmentPlacementServiceImageContext())
    class Meta:
        template = 'products/blocks/equipment_placement/service.html'
        label = 'Service'

class EquipmentPlacement(Page):
    body = StreamField([
        ('hero', HeroBlock()),
        ('floating_block', FloatingBlock()),
        ('equipment_placement_where_is_equipment', EquipmentPlacementWhereIsEquipment()),
        ('equipment_placement_service', EquipmentPlacementService()),
        ('faq', FAQBlock()),
        ('news', NewsList()),
        ('have_any_questions', HaveAnyQuestions()),
        ('advantages', Advantages()),
        ('video_block', VideoBlock()),

    ], null=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

class VmwareCloudConnectRepoItems(blocks.StructBlock):
    icon = ImageChooserBlock()
    title = blocks.CharBlock(required=True)
    body = blocks.CharBlock(required=True)
    
    class Meta:
        label = 'Repository '

class VmwareCloudConnectRepo(blocks.StructBlock):
    little_header = blocks.CharBlock(required=True)
    main_header = blocks.CharBlock(required=True)
    repo_items = blocks.ListBlock(VmwareCloudConnectRepoItems())

    class Meta:
        template = 'products/blocks/vmware_cloud_connect/repo.html'
        label = 'Repository'

class VeeamCloudAboutProduct(blocks.StructBlock):
    little_header = blocks.CharBlock(required=True)
    main_header = blocks.CharBlock(required=True)
    paragraph1 = blocks.CharBlock(required=True)
    paragraph_header = blocks.CharBlock(required=True)
    paragraph2 = blocks.CharBlock(required=True)
    icons = blocks.ListBlock(EquipmentPlacementIcons())
    bold_text = blocks.CharBlock(required=True)

    class Meta:
        template = 'products/blocks/vmware_cloud_connect/about_product.html'
        label = 'About Product'

class VmwareCloudConnect(Page):
    body = StreamField([
        ('hero', HeroBlock()),
        ('faq', FAQBlock()),
        ('news', NewsList()),
        ('have_any_questions', HaveAnyQuestions()),
        ('veeam_cloud_about_product', VeeamCloudAboutProduct()),
        ('advantages', Advantages()), 
        ('repository', VmwareCloudConnectRepo()),
        ('floating_block', FloatingBlock()),
        ('video_block', VideoBlock()),


    ], null=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

class RestoreVmwareCloudContext(blocks.StructBlock):
    paragraph_header = blocks.CharBlock()
    paragraph_context = blocks.CharBlock()
    image = ImageChooserBlock()

    class Meta:
        icon = 'TypeCloud'  # the icon that will appear in the admin
        label = 'TypeCloud'

class RestoreVmwareCloud(blocks.StructBlock):
    little_header = blocks.CharBlock(required=True)
    title = blocks.CharBlock(required=True)
    body = blocks.CharBlock(required=True)
    type_items = blocks.ListBlock(VmwareTypeCloudContext())

    class Meta:
        template = 'products/blocks/restore_vmware/cloud_type.html'
        label = 'Особенности решения'

class RestoreVmwareLittleScenarios(blocks.StructBlock):
    scenario_header = blocks.CharBlock(required=True)
    scenario_paragraph1 = blocks.CharBlock(required=True)
    image = ImageChooserBlock()
    scenario_paragraph2 = blocks.CharBlock(required=True)
    class Meta:
        label = 'Little Scenarios'

class RestoreVmwareBigScenarios(blocks.StructBlock):
    scenario_header = blocks.CharBlock(required=True)
    scenario_paragraph1 = blocks.CharBlock(required=True)
    image = ImageChooserBlock()
    scenario_paragraph2 = blocks.CharBlock(required=True)
    class Meta:
        label = 'Big Scenarios'

class RestoreVmwareScenario(blocks.StructBlock):
    little_header = blocks.CharBlock(required=True)
    main_header = blocks.CharBlock(required=True)
    little_scenarios = blocks.ListBlock(RestoreVmwareLittleScenarios())
    big_scenarios = blocks.ListBlock(RestoreVmwareBigScenarios())
    class Meta:
        template = 'products/blocks/restore_vmware/scenario.html'
        label = 'Scenario'

class DisasterRecoveryService(blocks.StructBlock):
    little_header = blocks.CharBlock(required=True)
    main_header = blocks.CharBlock(required=True)

    item1_icon = ImageChooserBlock()
    item1_title = blocks.CharBlock(required=True)
    item1_body = blocks.CharBlock(required=True)

    item2_icon = ImageChooserBlock()
    item2_title = blocks.CharBlock(required=True)
    item2_body = blocks.CharBlock(required=True)

    item3_icon = ImageChooserBlock()
    item3_title = blocks.CharBlock(required=True)
    item3_body = blocks.CharBlock(required=True)

    class Meta:
        template = 'products/blocks/restore_vmware/disaster_recovery.html'
        label = 'Disaster Recovery'

class RestoreVmwareBenefitsList(blocks.StructBlock):
    benefit = blocks.CharBlock(required=True)
    class Meta:
        label = 'Benefits List'

class RestoreVmwareBenefits(blocks.StructBlock):
    little_header = blocks.CharBlock(required=True)
    main_header = blocks.CharBlock(required=True)
    paragraph = blocks.CharBlock(required=True)
    context_header = blocks.CharBlock(required=True)
    context_list_items = blocks.ListBlock(RestoreVmwareBenefitsList())
    image = ImageChooserBlock()
    class Meta:
        template = 'products/blocks/restore_vmware/benefits.html'
        label = 'Benefits'

class RestoreVmware(Page):
    body = StreamField([
        ('hero', HeroBlock()),
        ('faq', FAQBlock()),
        ('news', NewsList()),
        ('floating_block', FloatingBlock()),
        ('have_any_questions', HaveAnyQuestions()),
        ('restore_vmware_scenario', RestoreVmwareScenario()),
        ('disaster_recovery', DisasterRecoveryService()),
        ('restore_vmware_benefits', RestoreVmwareBenefits()),
        ('restore_cloud', RestoreVmwareCloud()),
        ('video_block', VideoBlock()),
    ], null=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

class CloudMigrationFastAndSafe(blocks.StructBlock):
    little_header = blocks.CharBlock(required=True)
    main_header = blocks.CharBlock(required=True)
    paragraph1 = blocks.CharBlock(required=True)
    paragraph2 = blocks.CharBlock(required=True)
    image = ImageChooserBlock()
    class Meta:
        template = 'products/blocks/cloud_migration/fast_and_safe.html'
        label = 'Fast And Safe'

class CloudMigrationToCloudItems(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    body = blocks.CharBlock(required=True)
    
    class Meta:
        label = 'Pereezd'

class CloudMigrationToCloud(blocks.StructBlock):
    little_header = blocks.CharBlock(required=True)
    main_header = blocks.CharBlock(required=True)
    image = ImageChooserBlock()

    repo_items = blocks.ListBlock(CloudMigrationToCloudItems())

    class Meta:
        template = 'products/blocks/cloud_migration/to_cloud.html'
        label = 'To Cloud'

class CloudMigrationBenefitsIcons(blocks.StructBlock):
    icon = ImageChooserBlock()
    title = blocks.CharBlock(required=True)
    class Meta:
        label = 'Icons'

class CloudMigrationBenefits(blocks.StructBlock):
    little_header = blocks.CharBlock(required=True)
    main_header = blocks.CharBlock(required=True)
    paragraph = blocks.CharBlock(required=True)
    icons = blocks.ListBlock(CloudMigrationBenefitsIcons())

    class Meta:
        template = 'products/blocks/cloud_migration/benefits.html'
        label = 'Benefits'

class CloudMigration(Page):
    body = StreamField([
        ('hero', HeroBlock()),
        ('faq', FAQBlock()),
        ('news', NewsList()),
        ('floating_block', FloatingBlock()),
        ('have_any_questions', HaveAnyQuestions()),
        ('cloud_migration_fast_and_safe', CloudMigrationFastAndSafe()),
        ('to_pereezd', CloudMigrationToCloud()),
        ('cloud_migration_benefits', CloudMigrationBenefits()),
        ('video_block', VideoBlock()),
    ], null=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
    # http://127.0.0.1:8000/migraciya-v-oblako/