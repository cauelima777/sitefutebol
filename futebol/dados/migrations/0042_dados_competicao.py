# Generated by Django 4.2.1 on 2024-01-06 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dados', '0041_alter_dados_clube_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='dados',
            name='Competicao',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
