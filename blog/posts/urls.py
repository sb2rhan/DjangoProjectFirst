from django.urls import path
from posts import views
from posts import cbv_views

urlpatterns = [
    path('', cbv_views.IndexView.as_view(), name="main"), # name - to refer this page in html file
    path('<int:id>', cbv_views.DetailPostView.as_view(), name="details"),
    path('create', cbv_views.CreatePostView.as_view(), name="create"),
    path('edit/<int:id>', cbv_views.EditPostView.as_view(), name="edit"),
    path('delete/<int:id>', cbv_views.DeletePostView.as_view(), name="delete")
]
