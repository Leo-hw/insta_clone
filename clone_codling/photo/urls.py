from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', PhotoList.as_view(), name='index'),
    path('create/', PhotoCreate.as_view(), name ='create'),

    # view my post.
    path('mylist/', PhotoMyList.as_view(), name = 'mylist'),

    # like and favorite
    path('like/<int:photo_id>/', PhotoLike.as_view(), name = 'like'),
    path('favorite/<int:photo_id>/', PhotoFavorite.as_view(), name = 'favorite'),

    path('update/<int:pk>/', PhotoUpdate.as_view(), name ='update'),
    path('delete/<int:pk>/', PhotoDelete.as_view(), name ='delete'),
    path('detail/<int:pk>/', PhotoDetail.as_view(), name ='detail'),

    # view liked post and favorite 
    path('like/', PhotoLikeList.as_view(), name = 'like_list'),
    path('favorite/', PhotoFavoriteList.as_view(), name = 'like_list'),

]
