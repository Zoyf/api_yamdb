from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from reviews.models import Category, Genre
from .serializers import CategorySerializer, GenreSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
