from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Photo
from django.http.response import HttpResponseRedirect, HttpResponseForbidden
from django.contrib import messages

class PhotoList(ListView):
    model = Photo
    template_name_suffix = '_list'

class PhotoCreate(CreateView):
    model = Photo
    fields = ['text', 'image']
    template_name_suffix = '_create'
    success_url = '/'

class PhotoUpdate(UpdateView):
    model = Photo
    fields = ['text', 'image']
    template_name_suffix = '_update'
    success_url = '/'

class PhotoDelete(DeleteView):
    model = Photo
    success_url = '/'
    template_name_suffix = '_delete'

class PhotoDetail(DetailView):
    model = Photo
    success_url = '/'
    template_name_suffix = '_detail'
    
class PhotoMyList(ListView):
    model = Photo
    
     