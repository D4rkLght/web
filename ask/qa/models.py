
from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return Question

    def popular(self):
        return sorted(Question.rating)


class Question(models.Model):
    object = QuestionManager()
    title = models.CharField(max_length=225)
    text = models.TextField(User)
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name='question_like_user')


class Answer(models.Model):
    text = models.CharField(max_length=500)
    added_at = models.DateField()
    question = models.OneToOneField("Question", on_delete=models.PROTECT)
    author = models.CharField(max_length=40)
