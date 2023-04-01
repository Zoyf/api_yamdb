from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from reviews.models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.RegexField(
        regex=r'^[-a-zA-Z0-9_]+$',
        max_length=50,
        required=True,
        validators=[UniqueValidator(queryset=Category.objects.all())]
    )

    class Meta:
        model = Category
        fields = ('name', 'slug', 'description',)


class GenreSerializer(serializers.ModelSerializer):
    slug = serializers.RegexField(
        regex=r'^[-a-zA-Z0-9_]+$',
        max_length=50,
        required=True,
        validators=[UniqueValidator(queryset=Genre.objects.all())]
    )

    class Meta:
        model = Genre
        fields = ('name', 'slug', 'description',)


class TitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Title
        fields = ('__all__')
