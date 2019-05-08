from django.contrib import admin
from .models import Story, Tag
# Register your models here.


class StoryModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "tag", "photographer", "date", "draft"]
    list_display_links = ["__str__"]
    list_filter = ["date", "tag", "photographer", "draft"]

    class Meta:
        model = Story


admin.site.register(Story, StoryModelAdmin)
admin.site.register(Tag)
