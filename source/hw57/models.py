from django.db import models


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name='Тип задачи')

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name='Статус задачи')

    def __str__(self):
        return self.name


class Task(models.Model):
    summary = models.CharField(max_length=100, null=False, blank=False, verbose_name='Краткое описание')
    description = models.TextField(max_length=254, null=True, verbose_name='Полное описание')
    status = models.ForeignKey(to=Status, on_delete=models.PROTECT)
    type = models.ForeignKey(to=Type, on_delete=models.PROTECT)
    created_date = models.DateTimeField(verbose_name='Дата и время создания', auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name='Дата и время обновления', auto_now=True)
