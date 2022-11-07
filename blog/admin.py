from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Post, UserPostRelation


@admin.register(Post)
class PostAdmin(ModelAdmin):
    pass


@admin.register(UserPostRelation)
class UserPostRelationAdmin(ModelAdmin):
    pass

# admin.site.register(Post)
# admin.site.register(UserPostRelation)
