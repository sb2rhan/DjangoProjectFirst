from django.contrib import admin
from posts.models import Post, Tag

"""
    Register your models here.
    By registering we can see our models in the site
"""
# 1st way to register
# admin.site.register(Post)
# admin.site.register(Tag)

# 2nd and better way of registering a model because
# we can modify Post models page in admin panel
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'publish_date', 'status', 'author')
    search_fields = ['title', 'author', 'publish_date', 'status']
    list_filter = ('title', 'author', 'publish_date', 'status')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ['title', 'slug']
    list_filter = ('title', 'slug')
