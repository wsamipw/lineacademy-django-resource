from django.shortcuts import render
# from django.http import HttpResponse
from .forms import ContactForm
from .models import Article, Hero
from django.contrib import messages
# Create your views here.


def contactFormHandle(request):
    received = 0
    if request.method == 'POST':
        received = 1
        print("Form Received")
        form = ContactForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'You have successfully submitted your message.')
        else:
            messages.error(
                request, 'Error submitting your message. Please correct errors and Try again.')
    context = {
        "form": ContactForm()
    }
    return context


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
        "form": contactFormHandle(request)
    }
    return render(request, 'home/contact.html', context)
