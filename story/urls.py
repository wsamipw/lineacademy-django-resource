from django.urls import path

from . import views

app_name = 'story'

urlpatterns = [
    path('', views.story, name='story'),
    path('<slug:slug>/', views.story_detail, name='storyDetail'),
]
