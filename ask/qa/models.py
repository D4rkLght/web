
from django.db import models


class Answer(models.Model):
    text = models.CharField(max_length=500)
    added_at = models.DateField()
    question = models.OneToOneField()
    author = models.CharField(max_length=40)


class QuestionManager(models.Manager):
    def new(self):
        return Question

    def popular(self):
        return sorted(Question.rating)


class Question(models.Model):
    title = models.CharField(max_length=225)
    text = models.CharField(max_length=1000)
    added_at = models.DateField()
    rating = models.IntegerField()
    author = models.CharField(max_length=40)
    likes = models.ManyToManyField(Answer)
