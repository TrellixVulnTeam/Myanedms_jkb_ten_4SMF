# Generated by Django 2.2.24 on 2022-03-02 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logo_image', '0003_logo_logo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logo',
            options={'verbose_name': 'logo', 'verbose_name_plural': 'logo'},
        ),
        migrations.RemoveField(
            model_name='logo',
            name='name',
        ),
    ]
