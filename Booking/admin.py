# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.

from django.contrib import admin

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ['movie_name']
class TheaterAdmin(admin.ModelAdmin):
    list_display = ['theater_name']
class ShowAdmin(admin.ModelAdmin):
    list_display = ['show']
class ScreenAdmin(admin.ModelAdmin):
    list_display = ['screen']
class DateAdmin(admin.ModelAdmin):
    list_display = ['date']

admin.site.register(Theater, TheaterAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Show, ShowAdmin)
admin.site.register(Screen, ScreenAdmin)
admin.site.register(Date, DateAdmin)
admin.site.register(Booking)