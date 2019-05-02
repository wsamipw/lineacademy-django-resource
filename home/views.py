from django.shortcuts import render
from django.http import HttpResponse

from .models import Article
# Create your views here.


def index(request):
    article_list = Article.objects.all()
    print(article_list)
    context = {
        "articles": article_list
    }
    return render(request, 'home/index.html', context)
    # return HttpResponse("<h2>Hello, We have done it..</h2>")
