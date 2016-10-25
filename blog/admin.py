from django.contrib import admin
from .models import Post



class PostModelAdmin(admin.ModelAdmin):
    list_display=["title", "published date", "author"]
    search_field=["title", "content"]
admin.site.register(Post)

