from django.contrib import admin
from news.models import News
# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'content', 'publisher')
    list_filter = ('title', 'publish_date', 'publisher')
    search_fields = ['title', 'publisher']
