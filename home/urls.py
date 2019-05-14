from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('contact/update/<int:id>', views.contact_update, name="contact_update"),
    path('hero/create', views.hero_create, name='hearo_create'),
    path('hero/update/<int:id>', views.hero_update, name='hearo_update'),
]
