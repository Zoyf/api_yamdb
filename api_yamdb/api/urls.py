from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, GenreViewSet, ReviewViewSet, TitleViewSet

v1_router = DefaultRouter()

v1_router.register(r'v1/categories', CategoryViewSet)
v1_router.register(r'v1/genres', GenreViewSet)
v1_router.register(r'v1/titles', TitleViewSet)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)


urlpatterns = [
    path('', include(v1_router.urls)),
]
