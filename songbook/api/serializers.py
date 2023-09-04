import base64

from django.core.files.base import ContentFile
from songs.models import Book, Favorite, Group, Song, User
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        return super().to_internal_value(data)


class SongSerializer(serializers.ModelSerializer):
    added_by = SlugRelatedField(slug_field='username', read_only=True)
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        fields = '__all__'
        model = Song


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


# Разобраться, может подписки как избранное использовать
class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )
    favorites = serializers.SlugRelatedField(
        slug_field='favorites',
        queryset=Song.objects.all()
    )

    # def validate_favorites(self, value):
    #     if value == self.context['request'].user:
    #         raise serializers.ValidationError(
    #             'Нельзя подписаться на самого себя.')
    #     return value

    class Meta:
        fields = '__all__'
        model = Favorite
        validators = [
            UniqueTogetherValidator(
                queryset=Favorite.objects.all(),
                fields=('user', 'favorites'),
                message=('Уже добавлено в избранное.')
            )
        ]
