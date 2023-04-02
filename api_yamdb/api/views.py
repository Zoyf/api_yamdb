from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter


from reviews.models import Category, Genre, Title
from .serializers import (
    CategorySerializer,
    GenreSerializer,
    ReadTitleSerializer,
    CreateTitleSerializer
)
from .mixins import ListCreateDeleteViewSet


class CategoryViewSet(ListCreateDeleteViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(ListCreateDeleteViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = ReadTitleSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend,)
    filterset_fields = ('category', 'genre', 'year', 'name',)

    def get_serializer_class(self):
        if self.action in ['retrieve', 'list', 'destroy']:
            return ReadTitleSerializer
        return CreateTitleSerializer
