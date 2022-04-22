from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return Question

    def popular(self):
        return sorted(Question.rating)


class Question(models.Model):
    title = models.CharField(max_length=225)
    text = models.CharField(max_length=1000)
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.CharField(max_length=40)
    likes = models.ManyToManyField(User, related_name='question_like_user')


class Answer(models.Model):
    text = models.CharField(max_length=500)
    added_at = models.DateField()
    question = models.OneToOneField("Question", on_delete=models.PROTECT)
    author = models.CharField(max_length=40)
