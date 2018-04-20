from django.contrib import admin
from blogApp.models import *


@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_name', 'pub_date', 'post_text')
