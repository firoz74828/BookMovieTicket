# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Theater)
admin.site.register(Screen)
admin.site.register(Show)
admin.site.register(Date)
admin.site.register(Booking)
admin.site.register(Movie)
admin.site.register(Screen_Select)