# Generated by Django 2.1.7 on 2019-03-12 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hire_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Skills',
            new_name='Skill',
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'Cities'},
        ),
    ]