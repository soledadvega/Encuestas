import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200) #para campos de caract.
    pub_date = models.DateTimeField('date published') #var. de tiempo y fecha

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #fk define la relac. cd Choice se rel con 1 Question
    choice_text = models.CharField(max_length=200) #ChF. req.m_l se usa en BD y en validacion
    votes = models.IntegerField(default=0) #fija al default el valor de votes en 0

    def __str__(self):
        return self.choice_text
