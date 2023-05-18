from inspect import Parameter
from django.contrib import admin
from django.urls import path
from moviesite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.base),
    path('home',views.home),
    path('movie',views.movie),
    path('anime',views.anime),
    path('search',views.search),
    path('movieitem/(?P<val>\w+)/$',views.movieitem,name="movieitem"),
    path('animeitem/(?P<val>\w+)/$',views.animeitem,name="animeitem")
]