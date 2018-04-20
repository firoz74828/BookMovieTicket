# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.

from django.contrib import admin

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ['movie_name']
admin.site.register(Movie, MovieAdmin)
admin.site.register(Theater)
admin.site.register(Screen)
admin.site.register(Show)
admin.site.register(Date)
admin.site.register(Booking)
admin.site.register(Screen_Select)