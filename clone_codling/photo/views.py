from django.shortcuts import render, redirect
from django.views.generic.base import View
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

from urllib.parse import urlparse

class PhotoLike(View):
    def get(self, request, *args, **kwargs):
        
        # user check (login)
        if request.user.is_authenticated:
            return HttpResponseForbidden()
    
        else:
            if 'photo_id' in kwargs:
                photo_id = kwargs['photo_id']
                photo = Photo.objects.get(pk = 'photo_id')
                user = request.user
                if user in photo.like():
                    photo.like.remove(user)
                else:
                    photo.like.add(user)
            referer_url = request.META.get('HTTP_REFERER')
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)

class PhotoFavorite(View):
    def get(self, request, *args, **kwargs):
            
        # user check (login)
        if request.user.is_authenticated:
            return HttpResponseForbidden()
    
        else:
            if 'photo_id' in kwargs:
                photo_id = kwargs['photo_id']
                photo = Photo.objects.get(pk = 'photo_id')
                user = request.user
                if user in photo.favorite():
                    photo.favorite.remove(user)
                else:
                    photo.favorite.add(user)
            referer_url = request.META.get('HTTP_REFERER')
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)


class PhotoLikeList(ListView):
    model = Photo
    template_name = 'photo/photo_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, 'Please login first, before use this service')
            return HttpResponseRedirect('/')
        return super(PhotoLikeList, self).dispatch(request, *args, **kwargs)

    def get_query(self):
        user = self.request.user
        queryset = user.favorite_post.all()
        return queryset


class PhotoFavoriteList(ListView):
    model = Photo
    template_name = 'ptoto/photo_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, 'Please login, this service needs login before')
            return HttpResponseRedirect('/')
        return super(PhotoFavoriteList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        queryset = user.favorite_post.all()
        return queryset

# can use django decorator @login_required
# in this situation, don't have to make another class for mylist
'''
@login_required
def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos':photos})
'''


class PhotoMyList(ListView):
    model = Photo
    template_name = 'photo/photo_mylist.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, 'You need to login first')
            return HttpResponseRedirect('/')
        return super(PhotoMyList, self).dispatch(request, *args, **kwargs)
            