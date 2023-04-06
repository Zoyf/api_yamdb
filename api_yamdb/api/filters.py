from django_filters import rest_framework

from reviews.models import Title


class TitleFilter(rest_framework.FilterSet):
    category = rest_framework.CharFilter(field_name='category__slug')
    name = rest_framework.CharFilter(field_name='name',
                                     lookup_expr='icontains')
    genre = rest_framework.CharFilter(field_name='genre__slug')
    year = rest_framework.NumberFilter()

    class Meta:
        model = Title
        fields = ('category', 'genre', 'year', 'name',)
