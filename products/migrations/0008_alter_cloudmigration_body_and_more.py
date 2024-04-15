# Generated by Django 4.2.2 on 2023-06-18 20:22

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_cloudmigration_body_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloudmigration',
            name='body',
            field=wagtail.fields.StreamField([('hero', wagtail.blocks.StructBlock([('hero_title', wagtail.blocks.CharBlock(required=True)), ('hero_subtitle', wagtail.blocks.CharBlock(required=True)), ('hero_image', wagtail.images.blocks.ImageChooserBlock())])), ('faq', wagtail.blocks.StructBlock([('header', wagtail.blocks.CharBlock(required=True)), ('subtitle', wagtail.blocks.CharBlock(required=False)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('question', wagtail.blocks.CharBlock(required=True)), ('answer', wagtail.blocks.TextBlock(required=True))])))])), ('news', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Заголовок', required=True))])), ('floating_block', wagtail.blocks.StructBlock([('context', wagtail.blocks.CharBlock(required=True)), ('js_link', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock(required=True)))])), ('have_any_questions', wagtail.blocks.StructBlock([('header', wagtail.blocks.CharBlock(required=True)), ('subtitle', wagtail.blocks.CharBlock(required=True)), ('button_subtitle', wagtail.blocks.CharBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('cloud_migration_fast_and_safe', wagtail.blocks.StructBlock([('little_header', wagtail.blocks.CharBlock(required=True)), ('main_header', wagtail.blocks.CharBlock(required=True)), ('paragraph1', wagtail.blocks.CharBlock(required=True)), ('paragraph2', wagtail.blocks.CharBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('to_pereezd', wagtail.blocks.StructBlock([('little_header', wagtail.blocks.CharBlock(required=True)), ('main_header', wagtail.blocks.CharBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('repo_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('body', wagtail.blocks.CharBlock(required=True))])))])), ('cloud_migration_benefits', wagtail.blocks.StructBlock([('little_header', wagtail.blocks.CharBlock(required=True)), ('main_header', wagtail.blocks.CharBlock(required=True)), ('paragraph', wagtail.blocks.CharBlock(required=True)), ('icons', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(required=True))])))])), ('video_block', wagtail.blocks.StructBlock([('header', wagtail.blocks.CharBlock(required=True))]))], null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='equipmentplacement',
            name='body',
            field=wagtail.fields.StreamField([('hero', wagtail.blocks.StructBlock([('hero_title', wagtail.blocks.CharBlock(required=True)), ('hero_subtitle', wagtail.blocks.CharBlock(required=True)), ('hero_image', wagtail.images.blocks.ImageChooserBlock())])), ('floating_block', wagtail.blocks.StructBlock([('context', wagtail.blocks.CharBlock(required=True)), ('js_link', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock(required=True)))])), ('equipment_placement_where_is_equipment', wagtail.blocks.StructBlock([('little_header', wagtail.blocks.CharBlock(required=True)), ('main_header', wagtail.blocks.CharBlock(required=True)), ('paragraph', wagtail.blocks.CharBlock(required=True)), ('icons', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('icons_title', wagtail.blocks.CharBlock(required=True))]))), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('equipment_placement_service', wagtail.blocks.StructBlock([('little_header', wagtail.blocks.CharBlock(required=True)), ('main_header', wagtail.blocks.CharBlock(required=True)), ('paragraph', wagtail.blocks.CharBlock(required=True)), ('image_context', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('context', wagtail.blocks.CharBlock(required=True))])))])), ('faq', wagtail.blocks.StructBlock([('header', wagtail.blocks.CharBlock(required=True)), ('subtitle', wagtail.blocks.CharBlock(required=False)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('question', wagtail.blocks.CharBlock(required=True)), ('answer', wagtail.blocks.TextBlock(required=True))])))])), ('news', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Заголовок', required=True))])), ('have_any_questions', wagtail.blocks.StructBlock([('header', wagtail.blocks.CharBlock(required=True)), ('subtitle', wagtail.blocks.CharBlock(required=True)), ('button_subtitle', wagtail.blocks.CharBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('advantages', wagtail.blocks.StructBlock([('mini_header', wagtail.blocks.CharBlock(required=True)), ('header', wagtail.blocks.CharBlock(required=True)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(required=True)), ('subtitle', wagtail.blocks.CharBlock(required=True))]))), ('paragraph', wagtail.blocks.CharBlock(required=False))])), ('video_block', wagtail.blocks.StructBlock([('header', wagtail.blocks.CharBlock(required=True))]))], null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='reservecopy',
            name='body',
            field=wagtail.fields.StreamField([('faq', wagtail.blocks.StructBlock([('header', wagtail.blocks.CharBlock(required=True)), ('subtitle', wagtail.blocks.CharBlock(required=False)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('question', wagtail.blocks.CharBlock(required=True)), ('answer', wagtail.blocks.TextBlock(required=True))])))])), ('have_any_questions', wagtail.blocks.StructBlock([('header', wagtail.blocks.CharBlock(required=True)), ('subtitle', wagtail.blocks.CharBlock(required=True)), ('button_subtitle', wagtail.blocks.CharBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('hero', wagtail.blocks.StructBlock([('hero_title', wagtail.blocks.CharBlock(required=True)), ('hero_subtitle', wagtail.blocks.CharBlock(required=True)), ('hero_image', wagtail.images.blocks.ImageChooserBlock())])), ('advantages', wagtail.blocks.StructBlock([('mini_header', wagtail.blocks.CharBlock(required=True)), ('header', wagtail.blocks.CharBlock(required=True)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(required=True)), ('subtitle', wagtail.blocks.CharBlock(required=True))]))), ('paragraph', wagtail.blocks.CharBlock(required=False))])), ('reserve_copy_about_product', wagtail.blocks.StructBlock([('little_header', wagtail.blocks.CharBlock(required=True)), ('main_header', wagtail.blocks.CharBlock(required=True)), ('paragraph1', wagtail.blocks.CharBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('paragraph2', wagtail.blocks.CharBlock(required=True)), ('paragraph3', wagtail.blocks.CharBlock(required=True))])), ('reserve_copy_service', wagtail.blocks.StructBlock([('mini_header', wagtail.blocks.CharBlock(required=True)), ('header', wagtail.blocks.CharBlock(required=True)), ('table_rows', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('column1', wagtail.blocks.CharBlock(required=True)), ('column2', wagtail.blocks.CharBlock(required=True))]))), ('paragraph', wagtail.blocks.CharBlock(required=True))])), ('floating_block', wagtail.blocks.StructBlock([('context', wagtail.blocks.CharBlock(required=True)), ('js_link', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock(required=True)))])), ('video_block', wagtail.blocks.StructBlock([('header', wagtail.blocks.CharBlock(required=True))]))], null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='restorevmware',
            name='body',
            field=wagtail.fields.StreamField([('hero', wagtail.blocks.StructBlock([('hero_title', wagtail.blocks.CharBlock(required=True)), ('hero_subtitle', wagtail.blocks.CharBlock(required=True)), ('hero_image', wagtail.images.blocks.ImageChooserBlock())])), ('faq', wagtail.blocks.StructBlock([('header', wagtail.blocks.CharBlock(required=True)), ('subtitle', wagtail.blocks.CharBlock(required=False)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('question', wagtail.blocks.CharBlock(required=True)), ('answer', wagtail.blocks.TextBlock(required=True))])))])), ('news', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Заголовок', required=True))])), ('floating_block', wagtail.blocks.StructBlock([('context', wagtail.blocks.CharBlock(required=True)), ('js_link', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock(required=True)))])), ('have_any_questions', wagtail.blocks.StructBlock([('header', wagtail.blocks.CharBlock(required=True)), ('subtitle', wagtail.blocks.CharBlock(required=True)), ('button_subtitle', wagtail.blocks.CharBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('restore_vmware_scenario', wagtail.blocks.StructBlock([('little_header', wagtail.blocks.CharBlock(required=True)), ('main_header', wagtail.blocks.CharBlock(required=True)), ('little_scenarios', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('scenario_header', wagtail.blocks.CharBlock(required=True)), ('scenario_paragraph1', wagtail.blocks.CharBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('scenario_paragraph2', wagtail.blocks.CharBlock(required=True))]))), ('big_scenarios', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('scenario_header', wagtail.blocks.CharBlock(required=True)), ('scenario_paragraph1', wagtail.blocks.CharBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('scenario_paragraph2', wagtail.blocks.CharBlock(required=True))])))])), ('disaster_recovery', wagtail.blocks.StructBlock([('little_header', wagtail.blocks.CharBlock(required=True)), ('main_header', wagtail.blocks.CharBlock(required=True)), ('item1_icon', wagtail.images.blocks.ImageChooserBlock()), ('item1_title', wagtail.blocks.CharBlock(required=True)), ('item1_body', wagtail.blocks.CharBlock(required=True)), ('item2_icon', wagtail.images.blocks.ImageChooserBlock()), ('item2_title', wagtail.blocks.CharBlock(required=True)), ('item2_body', wagtail.blocks.CharBlock(required=True)), ('item3_icon', wagtail.images.blocks.ImageChooserBlock()), ('item3_title', wagtail.blocks.CharBlock(required=True)), ('item3_body', wagtail.blocks.CharBlock(required=True))])), ('restore_vmware_benefits', wagtail.blocks.StructBlock([('little_header', wagtail.blocks.CharBlock(required=True)), ('main_header', wagtail.blocks.CharBlock(required=True)), ('paragraph', wagtail.blocks.CharBlock(required=True)), ('context_header', wagtail.blocks.CharBlock(required=True)), ('context_list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('benefit', wagtail.blocks.CharBlock(required=True))]))), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('restore_cloud', wagtail.blocks.StructBlock([('little_header', wagtail.blocks.CharBlock(required=True)), ('title', wagtail.blocks.CharBlock(required=True)), ('body', wagtail.blocks.CharBlock(required=True)), ('type_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('paragraph_header', wagtail.blocks.CharBlock()), ('paragraph_context', wagtail.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])))])), ('video_block', wagtail.blocks.StructBlock([('header', wagtail.blocks.CharBlock(required=True))]))], null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='vmwarecloud',
            name='body',
            field=wagtail.fields.StreamField([('hero', wagtail.blocks.StructBlock([('hero_title', wagtail.blocks.CharBlock(required=True)), ('hero_subtitle', wagtail.blocks.CharBlock(required=True)), ('hero_image', wagtail.images.blocks.ImageChooserBlock())])), ('faq', wagtail.blocks.StructBlock([('header', wagtail.blocks.CharBlock(required=True)), ('subtitle', wagtail.blocks.CharBlock(required=False)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('question', wagtail.blocks.CharBlock(required=True)), ('answer', wagtail.blocks.TextBlock(required=True))])))])), ('floating_block', wagtail.blocks.StructBlock([('context', wagtail.blocks.CharBlock(required=True)), ('js_link', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock(required=True)))])), ('video_block', wagtail.blocks.StructBlock([('header', wagtail.blocks.CharBlock(required=True))])), ('advantages', wagtail.blocks.StructBlock([('mini_header', wagtail.blocks.CharBlock(required=True)), ('header', wagtail.blocks.CharBlock(required=True)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(required=True)), ('subtitle', wagtail.blocks.CharBlock(required=True))]))), ('paragraph', wagtail.blocks.CharBlock(required=False))])), ('have_any_questions', wagtail.blocks.StructBlock([('header', wagtail.blocks.CharBlock(required=True)), ('subtitle', wagtail.blocks.CharBlock(required=True)), ('button_subtitle', wagtail.blocks.CharBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('news', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Заголовок', required=True))])), ('vmware_cloud_comparison', wagtail.blocks.StructBlock([('little_header', wagtail.blocks.CharBlock(required=True)), ('main_header', wagtail.blocks.CharBlock(required=True)), ('paragraphs', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title_paragraph', wagtail.blocks.CharBlock(required=True)), ('context_paragraph', wagtail.blocks.CharBlock(required=True))]))), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('vmware_cloud_peculiarities', wagtail.blocks.StructBlock([('little_header', wagtail.blocks.CharBlock(required=True)), ('main_header', wagtail.blocks.CharBlock(required=True)), ('paragraph_header', wagtail.blocks.CharBlock(required=True)), ('paragraph_context', wagtail.blocks.CharBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('icons_header', wagtail.blocks.CharBlock(required=True)), ('icons', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('icons_title', wagtail.blocks.CharBlock(required=True))])))])), ('vmware_type', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('body', wagtail.blocks.CharBlock(required=True)), ('type_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('paragraph_header', wagtail.blocks.CharBlock()), ('paragraph_context', wagtail.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])))])), ('vmware_type_black', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('body', wagtail.blocks.CharBlock(required=True)), ('type_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('paragraph_header', wagtail.blocks.CharBlock()), ('paragraph_context', wagtail.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])))]))], null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='vmwarecloudconnect',
            name='body',
            field=wagtail.fields.StreamField([('hero', wagtail.blocks.StructBlock([('hero_title', wagtail.blocks.CharBlock(required=True)), ('hero_subtitle', wagtail.blocks.CharBlock(required=True)), ('hero_image', wagtail.images.blocks.ImageChooserBlock())])), ('faq', wagtail.blocks.StructBlock([('header', wagtail.blocks.CharBlock(required=True)), ('subtitle', wagtail.blocks.CharBlock(required=False)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('question', wagtail.blocks.CharBlock(required=True)), ('answer', wagtail.blocks.TextBlock(required=True))])))])), ('news', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(label='Заголовок', required=True))])), ('have_any_questions', wagtail.blocks.StructBlock([('header', wagtail.blocks.CharBlock(required=True)), ('subtitle', wagtail.blocks.CharBlock(required=True)), ('button_subtitle', wagtail.blocks.CharBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('veeam_cloud_about_product', wagtail.blocks.StructBlock([('little_header', wagtail.blocks.CharBlock(required=True)), ('main_header', wagtail.blocks.CharBlock(required=True)), ('paragraph1', wagtail.blocks.CharBlock(required=True)), ('paragraph_header', wagtail.blocks.CharBlock(required=True)), ('paragraph2', wagtail.blocks.CharBlock(required=True)), ('icons', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('icons_title', wagtail.blocks.CharBlock(required=True))]))), ('bold_text', wagtail.blocks.CharBlock(required=True))])), ('advantages', wagtail.blocks.StructBlock([('mini_header', wagtail.blocks.CharBlock(required=True)), ('header', wagtail.blocks.CharBlock(required=True)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(required=True)), ('subtitle', wagtail.blocks.CharBlock(required=True))]))), ('paragraph', wagtail.blocks.CharBlock(required=False))])), ('repository', wagtail.blocks.StructBlock([('little_header', wagtail.blocks.CharBlock(required=True)), ('main_header', wagtail.blocks.CharBlock(required=True)), ('repo_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(required=True)), ('body', wagtail.blocks.CharBlock(required=True))])))])), ('floating_block', wagtail.blocks.StructBlock([('context', wagtail.blocks.CharBlock(required=True)), ('js_link', wagtail.blocks.ListBlock(wagtail.blocks.CharBlock(required=True)))])), ('video_block', wagtail.blocks.StructBlock([('header', wagtail.blocks.CharBlock(required=True))]))], null=True, use_json_field=True),
        ),
    ]
