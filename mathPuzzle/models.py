import datetime

from django.contrib.auth.models import User
from django.db import models
import django.utils.timezone as timezone


class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name="Задача")
    LOTO = 'LOTO'
    CARDS = 'CARDS'
    TEST = 'TEST'
    type_choices = (
        (LOTO, 'Лото'),
        (CARDS, 'Карточки'),
        (TEST, 'Тест')
    )
    type = models.CharField(verbose_name="Тип", max_length=10, choices=type_choices, default=TEST)
    date_published = models.DateTimeField(verbose_name="Дата публикации", default=datetime.datetime.now())

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'


class TaskResult(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField(verbose_name="Время ответа", default=timezone.now())


class Question(models.Model):
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name="Номер вопроса", default=1)
    title = models.CharField(max_length=200, verbose_name="Вопрос", default="question")
    date_published = models.DateTimeField(verbose_name="Дата публикации", default=timezone.now())

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200, verbose_name="Ответ", default="answer")
    is_right = models.BooleanField(verbose_name="Верный ответ?")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
