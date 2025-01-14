# Generated by Django 4.2.1 on 2023-06-01 01:02

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restorevmware',
            name='body',
            field=wagtail.fields.StreamField([('hero', wagtail.blocks.StructBlock([('hero_title', wagtail.blocks.CharBlock(required=True)), ('hero_subtitle', wagtail.blocks.CharBlock(required=True)), ('hero_image', wagtail.images.blocks.ImageChooserBlock())])), ('faq', wagtail.blocks.StructBlock([('header', wagtail.blocks.CharBlock(required=True)), ('subtitle', wagtail.blocks.CharBlock(required=False)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('question', wagtail.blocks.CharBlock(required=True)), ('answer', wagtail.blocks.TextBlock(required=True))])))])), ('news', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True))])), ('floating_block', wagtail.blocks.StructBlock([('context', wagtail.blocks.CharBlock(required=True)), ('js_link', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock(required=True)))])), ('have_any_questions', wagtail.blocks.StructBlock([('header', wagtail.blocks.CharBlock(required=True)), ('subtitle', wagtail.blocks.CharBlock(required=True)), ('button_subtitle', wagtail.blocks.CharBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('restore_vmware_scenario', wagtail.blocks.StructBlock([('little_header', wagtail.blocks.CharBlock(required=True)), ('main_header', wagtail.blocks.CharBlock(required=True)), ('little_scenarios', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('scenario_header', wagtail.blocks.CharBlock(required=True)), ('scenario_paragraph1', wagtail.blocks.CharBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('scenario_paragraph2', wagtail.blocks.CharBlock(required=True))]))), ('big_scenarios', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('scenario_header', wagtail.blocks.CharBlock(required=True)), ('scenario_paragraph1', wagtail.blocks.CharBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('scenario_paragraph2', wagtail.blocks.CharBlock(required=True))])))])), ('disaster_recovery', wagtail.blocks.StructBlock([('little_header', wagtail.blocks.CharBlock(required=True)), ('main_header', wagtail.blocks.CharBlock(required=True)), ('item1_icon', wagtail.images.blocks.ImageChooserBlock()), ('item1_title', wagtail.blocks.CharBlock(required=True)), ('item1_body', wagtail.blocks.CharBlock(required=True)), ('item2_icon', wagtail.images.blocks.ImageChooserBlock()), ('item2_title', wagtail.blocks.CharBlock(required=True)), ('item2_body', wagtail.blocks.CharBlock(required=True)), ('item3_icon', wagtail.images.blocks.ImageChooserBlock()), ('item3_title', wagtail.blocks.CharBlock(required=True)), ('item3_body', wagtail.blocks.CharBlock(required=True))])), ('restore_vmware_benefits', wagtail.blocks.StructBlock([('little_header', wagtail.blocks.CharBlock(required=True)), ('main_header', wagtail.blocks.CharBlock(required=True)), ('paragraph', wagtail.blocks.CharBlock(required=True)), ('context_header', wagtail.blocks.CharBlock(required=True)), ('context_list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('benefit', wagtail.blocks.CharBlock(required=True))]))), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('restore_cloud', wagtail.blocks.StructBlock([('little_header', wagtail.blocks.CharBlock(required=True)), ('title', wagtail.blocks.CharBlock(required=True)), ('body', wagtail.blocks.CharBlock(required=True)), ('type_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('paragraph_header', wagtail.blocks.CharBlock()), ('paragraph_context', wagtail.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])))]))], null=True, use_json_field=True),
        ),
    ]
