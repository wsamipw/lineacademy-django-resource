from django.shortcuts import render, get_object_or_404


# Create your views here.
from .models import Story, Tag


def story(request):
    story_list = Story.objects.all()
    tag_list = Tag.objects.all()
    context = {
        "story_list": story_list,
        "tag_list": tag_list

    }
    return render(request, 'story/story.html', context)


def story_detail(request, slug=None):
    instance = get_object_or_404(Story, slug=slug)
    context = {
        "instance": instance
    }
    return render(request, 'story/story-detail.html', context)


def story_tag(request, name=None):
    story_list = Story.objects.filter(tag__name=name)
    tag_list = Tag.objects.all()
    context = {
        "story_list": story_list,
        "tag_list": tag_list,
        "name": name
    }
    return render(request, 'story/tag-story.html', context)
