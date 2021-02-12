from clone_codling.accounts.views import signup
from django.contrib import admin
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    
 
]