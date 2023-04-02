from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from permissions import IsAdminOrModeratorOrReadOnly
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from reviews.models import Category, Genre, Title

from .mixins import ListCreateDeleteViewSet
from .serializers import (CategorySerializer, CreateTitleSerializer,
                          GenreSerializer, ReadTitleSerializer,
                          ReviewSerializer)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminOrModeratorOrReadOnly, ]

    def get_queryset(self):
        title_id = self.kwargs.get("title_id")
        title = get_object_or_404(Title, id=title_id)
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get("title_id"))
        serializer.save(author=self.request.user, title=title)

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
