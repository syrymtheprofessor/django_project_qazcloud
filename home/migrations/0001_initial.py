# Generated by Django 4.2.1 on 2023-05-31 09:46

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='RootPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.fields.StreamField([('root_page_hero_block', wagtail.blocks.StructBlock([('main_header', wagtail.blocks.CharBlock(required=True)), ('subtitle_header', wagtail.blocks.CharBlock(required=True)), ('btn_text', wagtail.blocks.CharBlock(required=False)), ('hero_image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('faq', wagtail.blocks.StructBlock([('header', wagtail.blocks.CharBlock(required=True)), ('subtitle', wagtail.blocks.CharBlock(required=False)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('question', wagtail.blocks.CharBlock(required=True)), ('answer', wagtail.blocks.TextBlock(required=True))])))])), ('have_any_questions', wagtail.blocks.StructBlock([('header', wagtail.blocks.CharBlock(required=True)), ('subtitle', wagtail.blocks.CharBlock(required=True)), ('button_subtitle', wagtail.blocks.CharBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('root_page_products', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(required=True)), ('description', wagtail.blocks.CharBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('link_page', wagtail.blocks.PageChooserBlock(required=False))])))])), ('news_list', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True))])), ('root_page_clients', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('images', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))])))])), ('root_page_feature_services', wagtail.blocks.StructBlock([('main_header', wagtail.blocks.CharBlock(required=True)), ('icons', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(required=True))]))), ('slider', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))])))])), ('root_page_why_choose_us', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(required=True)), ('description', wagtail.blocks.CharBlock(required=True))])))]))], null=True, use_json_field=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
