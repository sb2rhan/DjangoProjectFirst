from django.urls import path, include
from rest_framework import routers

from .views import TodoViewSet

# Router will get all routes of urls
router = routers.DefaultRouter()
router.register('todo', TodoViewSet)
urlpatterns = [
    path('', include(router.urls))
]
