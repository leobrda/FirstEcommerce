# Generated by Django 5.1.3 on 2024-11-09 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_alter_produto_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='')),
                ('link_destino', models.CharField(blank=True, max_length=400, null=True)),
                ('ativo', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banners',
            },
        ),
        migrations.AlterModelOptions(
            name='itemestoque',
            options={'verbose_name': 'Item Estoque', 'verbose_name_plural': 'Itens Estoque'},
        ),
    ]
