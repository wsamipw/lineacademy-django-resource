from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    context = {
        "name": "samip subedi",
        "address": "pokhara"
    }
    return render(request, 'home/index.html', context)
    # return HttpResponse("<h2>Hello, We have done it..</h2>")
