from django.shortcuts import render, get_object_or_404


# Create your views here.
from .models import Story, Tag


def story(request):
    story_list = Story.objects.all()
    context = {
        "story_list": story_list

    }
    return render(request, 'story/story.html', context)


def story_detail(request, slug=None):
    instance = get_object_or_404(Story, slug=slug)
    context = {
        "instance": instance
    }
    return render(request, 'story/story-detail.html', context)
