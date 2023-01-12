# Generated by Django 4.1.4 on 2022-12-16 14:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dialog',
            options={'ordering': ['name'], 'verbose_name': 'Диалог', 'verbose_name_plural': 'Диалоги'},
        ),
        migrations.AlterField(
            model_name='dialog',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Имя диалога'),
        ),
        migrations.AlterField(
            model_name='dialog',
            name='online',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='онлайн'),
        ),
    ]