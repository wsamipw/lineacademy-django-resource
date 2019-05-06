from django.contrib import admin
from .models import Article, Hero, Story, Tag
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


class StoryModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "tag", "photographer", "date", "draft"]
    list_display_links = ["__str__"]
    list_filter = ["date", "tag", "photographer", "draft"]

    class Meta:
        model = Story


admin.site.register(Article, ArticleModelAdmin)
admin.site.register(Hero, HeroModelAdmin)
admin.site.register(Story, StoryModelAdmin)
admin.site.register(Tag)
