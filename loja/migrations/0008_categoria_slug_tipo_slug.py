# Generated by Django 5.1.3 on 2024-11-25 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0007_alter_itemestoque_cor'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='tipo',
            name='slug',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
