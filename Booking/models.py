# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Theater(models.Model):
    theater_name = models.CharField(max_length=30)
    theater_image = models.ImageField(upload_to='', blank=True, null=True)
    def __unicode__(self):
        return self.theater_name

class Movie(models.Model):
    movie_name = models.CharField(max_length=30)
    movie_image = models.ImageField(upload_to='', blank=True, null=True)
    def __unicode__(self):
        return self.movie_name

class Show(models.Model):
    show = models.CharField(max_length=30)
    def __unicode__(self):
        return self.show

class Date(models.Model):
    date = models.DateField(default=datetime.now())
    def __unicode__(self):
        return unicode(self.date)

class Screen(models.Model):
    screen = models.CharField(max_length=20)
    def __unicode__(self):
        return self.screen


class Screen_Select(models.Model):
    theater_screen_id = models.ForeignKey(Theater, on_delete=models.CASCADE)
    movie_screen_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    show_screen_id = models.ForeignKey(Show, on_delete=models.CASCADE)
    screen_id = models.ForeignKey(Screen, on_delete=models.CASCADE)
    date_screen_id = models.ForeignKey(Date, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("theater_screen_id", "show_screen_id", "screen_id" ,"date_screen_id")



class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    theater_id = models.ForeignKey(Theater,on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    show_id = models.ForeignKey(Show, on_delete=models.CASCADE)
    screen_id = models.ForeignKey(Screen,on_delete=models.CASCADE)
    seat = models.CharField(max_length=20)
    date_id  = models.ForeignKey(Date, on_delete=models.CASCADE)
    date_today = models.DateTimeField(default=datetime.now, editable=False)

    class Meta:
        unique_together = ("theater_id", "movie_id", "show_id" ,"screen_id", "seat", "date_id")










