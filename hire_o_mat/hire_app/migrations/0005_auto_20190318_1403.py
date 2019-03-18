# Generated by Django 2.1.7 on 2019-03-18 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hire_app', '0004_auto_20190318_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='company',
        ),
        migrations.AddField(
            model_name='companyprofile',
            name='positions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hire_app.Position'),
        ),
    ]
