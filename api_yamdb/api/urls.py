from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import APIGetToken, APISignup, UsersViewSet, CategoryViewSet, GenreViewSet, TitleViewSet

router = SimpleRouter()

router.register(
    'users',
    UsersViewSet,
    basename='users'
)
router.register(r'categories', CategoryViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'titles', TitleViewSet)


urlpatterns = [
    path('v1/auth/token/', APIGetToken.as_view(), name='get_token'),
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', APISignup.as_view(), name='signup'),
]
