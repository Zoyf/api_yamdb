<<<<<<< HEAD
from rest_framework.routers import DefaultRouter
from views import CommentViewSet

router = DefaultRouter()
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
=======
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
>>>>>>> 86d9969409bbf6d5db32e57cfdb9afc90ebc3b4d
