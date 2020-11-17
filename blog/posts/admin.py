from django.contrib import admin
from posts.models import Post, Tag

"""
    Register your models here.
    By registering we can see our models in the site
"""
# Old way to register

# admin.site.register(Post)
admin.site.register(Tag)

# for controlling Post models page in admin panel (new way)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'publish_date', 'status', 'author')
    search_fields = ['title', 'author', 'publish_date', 'status']

