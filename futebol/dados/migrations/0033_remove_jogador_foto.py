# Generated by Django 4.2.1 on 2023-07-28 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dados', '0032_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jogador',
            name='foto',
        ),
    ]
