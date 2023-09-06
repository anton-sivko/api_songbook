from django.contrib import admin
from django.contrib.admin import register
from songs.models import (Book, Favorite, Group, Song)


@register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'author')
    search_fields = ('name', )
    fields = (
        'name', 'text', 'group', 'book',
        'image', 'author', 'in_favorites'
    )
    readonly_fields = ('in_favorites', 'added_by')
    list_filter = ('name', 'author')

    @admin.display(description='В избранном')
    def in_favorites(self, obj):
        return obj.favorite_song.count()


# @register(Ingredient)
# class IngredientAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'name', 'measurement_unit')
#     list_filter = ('name', )
#     search_fields = ('name', )


# @register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'name', 'color', 'slug')
#     list_editable = ('name', 'color', 'slug')


# @register(IngredientAmount)
# class IngredientAmountAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'recipe', 'ingredient', 'amount')
#     list_editable = ('recipe', 'ingredient', 'amount')


# @register(Favorite)
# class FavoriteAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'user', 'favorite_recipe')
#     list_editable = ('user', 'favorite_recipe')


# @register(ShoppingCart)
# class ShoppingCartAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'user', 'recipe')
#     list_editable = ('user', 'recipe')