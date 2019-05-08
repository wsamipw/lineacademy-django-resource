from django.shortcuts import render
# from django.http import HttpResponse

from .models import Article, Hero
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


def contact(request):
    context = {

    }
    return render(request, 'home/contact.html', context)
