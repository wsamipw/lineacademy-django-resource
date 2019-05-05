from django.contrib import admin
from .models import Article, Hero
# Register your models here.


class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "date", "draft"]
    list_display_links = ["__str__"]
    list_editable = ["draft"]
    list_filter = ["date", "draft"]

    class Meta:
        model = Article


class HeroModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "caption", "date"]
    list_display_links = ["__str__"]
    list_filter = ["date"]

    class Meta:
        model = Hero


admin.site.register(Article, ArticleModelAdmin)
admin.site.register(Hero, HeroModelAdmin)
