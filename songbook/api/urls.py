from api.views import FavoriteViewset, GroupViewSet, SongViewSet
from django.urls import include, path
from rest_framework import routers

v1_router = routers.DefaultRouter()
v1_router.register(r'groups', GroupViewSet)
v1_router.register(r'songs', SongViewSet)
v1_router.register(r'favorite', FavoriteViewset)


urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
