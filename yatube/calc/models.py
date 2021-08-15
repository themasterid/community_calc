from django.db import models
import datetime


class Bb(models.Model):
    ammount = models.FloatField(
        null=True,
        blank=True,
        verbose_name='Цена')
    comment = models.CharField(
        max_length=50,
        verbose_name='Коментарий')
    published = models.DateField(
        auto_now_add=False,
        db_index=False,
        verbose_name='Опубликовано')

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ['-published']
        verbose_name_plural = 'Записи'
        verbose_name = 'Запись'
