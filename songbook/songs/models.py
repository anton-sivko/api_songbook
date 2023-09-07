from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Song(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    added_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='songs', null=True)
    image = models.ImageField(
        upload_to='songs/', null=True, blank=True)
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name="songs", blank=True, null=True
    )
    book = models.ForeignKey(
        Book, on_delete=models.SET_NULL,
        related_name="songs", blank=True, null=True
    )

    def __str__(self):
        return self.text[:15]


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
    )
    favorites = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Любимая песня',
    )

    def __repr__(self):
        return self.text

    def __str__(self) -> str:
        return self.text

    class Meta:
        ordering = ['-favorites']
        constraints = [models.UniqueConstraint(
            fields=['user', 'favorites'],
            name='unique following')
        ]
