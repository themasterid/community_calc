from django.contrib.auth import get_user_model

from django.db import models


User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='ЧПУ')
    description = models.TextField(max_length=400, verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Группы'
        verbose_name = 'Группа'


class Post(models.Model):
    text = models.TextField(
        max_length=400,
        verbose_name='Текст'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts'
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'


class Calc(models.Model):
    ammount = models.IntegerField(
        verbose_name='Значение'
    )
    comment = models.CharField(
        max_length=100,
        verbose_name='Коментарий'
    )
    date = models.DateField(
        auto_now_add=False,
        verbose_name='Дата'
    )

    class Meta:
        verbose_name_plural = 'Значения'

    def __str__(self):
        return self.comment
