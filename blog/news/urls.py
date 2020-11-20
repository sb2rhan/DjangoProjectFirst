from django.urls import path
from news import views

urlpatterns = [
    path('news', views.all_news, name="news"),
    path('news/<int:id>', views.news_info, name="info"),
    path('news/create', views.create_news, name="news_create")
]
