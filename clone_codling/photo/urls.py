from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', PhotoList.as_view(), name='index'),
    path('create/<int:pk>/', PhotoCreate.as_view(), name ='create'),
    path('update/<int:pk>/', PhotoUpdate.as_view(), name ='update'),
    path('delete/<int:pk>/', PhotoDelete.as_view(), name ='delete'),
    path('detail/<int:pk>/', PhotoDetail.as_view(), name ='detail'),
]
