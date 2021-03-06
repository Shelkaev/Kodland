# Generated by Django 3.1.3 on 2020-11-28 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleApply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(help_text='Загрузите фотографию', upload_to='', verbose_name='Иллюстрация')),
                ('name', models.CharField(help_text='Введите имя', max_length=255, verbose_name='Название поста')),
                ('date', models.DateField(auto_now_add=True)),
                ('article', models.TextField(blank=True, help_text='Введите текст', null=True, verbose_name='Текст статьи')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
