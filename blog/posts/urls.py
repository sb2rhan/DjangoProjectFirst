from django.urls import path
from posts import views

urlpatterns = [
    path('', views.index, name="main"), # name - to refer this page in html file
    path('<int:id>', views.detail, name="details"),
    path('create', views.create_post, name="create"),
    path('edit/<int:id>', views.edit_post, name="edit"),
    path('delete/<int:id>', views.delete_post, name="delete")
]
