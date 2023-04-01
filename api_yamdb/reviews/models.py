from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True, max_length=50)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name[:20]


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True, max_length=50)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name[:20]


class Title(models.Model):
    name = models.CharField(max_length=256)
    year = models.DateTimeField()
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        blank=True, null=True
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        related_name='titles',
        blank=True, null=True
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name[:30]
