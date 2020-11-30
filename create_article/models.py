from django.db import models


# Create your models here.
class ArticleApply(models.Model):
    photo = models.ImageField(verbose_name='Иллюстрация', max_length=100, help_text='Загрузите фотографию')
    name = models.CharField(verbose_name='Название поста', max_length=255, help_text='Введите название статьи')
    date = models.DateField(auto_now_add=True)
    article = models.TextField(null=True, blank=True,
                               help_text='Введите текст',
                               verbose_name='Текст статьи')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.name
