# Generated by Django 5.0.6 on 2024-06-05 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0007_alter_competencia_options_alter_entrenador_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='competencia',
            options={'verbose_name': 'Competencia', 'verbose_name_plural': 'Competencias'},
        ),
    ]