# Generated by Django 4.2.1 on 2023-06-01 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QazcloudMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title', models.CharField(blank=True, max_length=512, null=True)),
                ('about_context', models.CharField(blank=True, max_length=512, null=True)),
                ('career_title', models.CharField(blank=True, max_length=512, null=True)),
                ('career_context', models.CharField(blank=True, max_length=512, null=True)),
                ('law_info', models.CharField(blank=True, max_length=512, null=True)),
                ('law_context', models.CharField(blank=True, max_length=512, null=True)),
                ('law_address', models.CharField(blank=True, max_length=512, null=True)),
                ('law_address_name', models.CharField(blank=True, max_length=512, null=True)),
                ('law_address_address', models.CharField(blank=True, max_length=512, null=True)),
                ('law_contract1', models.CharField(blank=True, max_length=512, null=True)),
                ('law_contract2', models.CharField(blank=True, max_length=512, null=True)),
                ('address_title', models.CharField(blank=True, max_length=512, null=True)),
                ('address_name1', models.CharField(blank=True, max_length=512, null=True)),
                ('address_address1', models.CharField(blank=True, max_length=512, null=True)),
                ('address_name2', models.CharField(blank=True, max_length=512, null=True)),
                ('address_address2', models.CharField(blank=True, max_length=512, null=True)),
                ('address_name3', models.CharField(blank=True, max_length=512, null=True)),
                ('address_address3', models.CharField(blank=True, max_length=512, null=True)),
                ('contacts_contacts_title', models.CharField(blank=True, max_length=512, null=True)),
                ('contacts_tech_title', models.CharField(blank=True, max_length=512, null=True)),
                ('contacts_tech_number', models.CharField(blank=True, max_length=512, null=True)),
                ('contacts_sales_title', models.CharField(blank=True, max_length=512, null=True)),
                ('contacts_sales_number', models.CharField(blank=True, max_length=512, null=True)),
                ('press_mail', models.CharField(blank=True, max_length=512, null=True)),
                ('press_context', models.CharField(blank=True, max_length=512, null=True)),
                ('logo1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('logo2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
        ),
    ]