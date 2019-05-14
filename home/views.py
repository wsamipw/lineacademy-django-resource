from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from .forms import ContactForm, HeroForm
from .models import Article, Hero, Contact
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


# @login_required(login_url='admin/')
# def hero_create(request):


def contact(request):
    context = {
        # "form": contactFormHandle(request)
    }
    return render(request, 'home/contact.html', context)


@login_required(login_url='/admin/login/')
def hero_create(request):
    form = HeroForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(
                request, 'You have successfully created Hero Slider.')
        else:
            messages.error(
                request, 'Error creating hero slider. Please correct errors and Try again.')
    context = {
        "form": form
    }
    return render(request, 'home/hero_create.html', context)


@login_required(login_url='/admin/login/')
def hero_update(request, id=None):
    instance = get_object_or_404(Hero, id=id)
    form = HeroForm(request.POST or None,
                    request.FILES or None, instance=instance)
    print(form)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(
                request, 'You have successfully updated Hero Slider.')
        else:
            messages.error(
                request, 'Error updating hero slider. Please correct errors and Try again.')
    context = {
        "instance": instance,
        "form": form,
        "update": True
    }
    return render(request, 'home/hero_create.html', context)


@login_required(login_url='/admin/login/')
def contact_update(request, id=None):
    instance = get_object_or_404(Contact, id=id)
    form = ContactForm(request.POST or None,
                       request.FILES or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(
                request, 'You have successfully updated your message.')
        else:
            messages.error(
                request, 'Error updating your message. Please correct errors and Try again.')

    context = {
        "instance": instance,
        "form": form
    }
    return render(request, 'home/contact.html', context)
