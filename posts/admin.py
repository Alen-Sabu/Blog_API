from django.contrib import admin
from posts.models import Category, Comment, Post
# Register your models here.

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
