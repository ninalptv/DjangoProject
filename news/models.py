from django.db import models


class InterestingFacts(models.Model):
    title = models.CharField('Название', max_length=100, default='')
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Основной текст')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Факт'
        verbose_name_plural = 'Факты'