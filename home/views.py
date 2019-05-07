from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Article, Hero, Story
# Create your views here.


def index(request):
    article_list = Article.objects.all()
    hero_list = Hero.objects.all()
    print(article_list)
    context = {
        "articles": article_list,
        "hero_list": hero_list
    }
    return render(request, 'home/index.html', context)
    # return HttpResponse("<h2>Hello, We have done it..</h2>")


def story(request):
    story_list = Story.objects.all()
    context = {
        "story_list": story_list

    }
    return render(request, 'home/story.html', context)


def story_detail(request, slug=None):
    instance = get_object_or_404(Story, slug=slug)
    context = {
        "instance": instance
    }
    return render(request, 'home/story-detail.html', context)


def contact(request):
    context = {

    }
    return render(request, 'home/contact.html', context)
