from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, GenreViewSet

v1_router = DefaultRouter()

v1_router.register(r'v1/categories', CategoryViewSet)
v1_router.register(r'v1/genres', GenreViewSet)


urlpatterns = [
    path('', include(v1_router.urls)),
]
