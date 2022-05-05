from django.http import Http404
from django.core.paginator import Paginator
from django.shortcuts import render


from . import models


def home(request, *args, **kwargs):
    questions_list = models.QuestionManager.new(models.Question.objects.all())
    paginator = Paginator(questions_list, 10)

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'index.html', {'posts': posts})


def ask(request, *args, **kwargs):

    return render(request, 'ask.html')


def popular(request, *args, **kwargs):
    questions_list = models.QuestionManager.popular(
        models.Question.objects.all())
    paginator = Paginator(questions_list, 10)

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'popular.html', {'posts': posts})


def question(request, *args, **kwargs):
    posts = models.Question.objects.all()
    post_id = request.path.split('/')[-2]
    for post in posts:
        if post.id == int(post_id):
            return render(request, 'question.html', {'post': post})
