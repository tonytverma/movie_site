from django.contrib import admin

from moviesite.models import createanime, createmovies
# Register your models here.
admin.site.register(createmovies)
admin.site.register(createanime)