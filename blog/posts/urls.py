from django.http import HttpResponse
from django.urls import path
from posts import views

urlpatterns = [
    path('', views.index, name="main"), # name - to refer this page in html file
    path('<int:id>', views.detail, name="details"),
    path('create', views.create, name="create"),
    path('edit/<int:id>', views.edit, name="edit")
]
