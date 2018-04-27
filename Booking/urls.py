from django.conf.urls import url
from .views import *
from .import views

app_name = 'Booking'
urlpatterns = [

    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^login-page/$', LoginPage.as_view(), name = 'login-page'),
    # url(r'^seat-booked/$', views.Seat_Booked, name = 'seat-booked'),
    url(r'^google-chart/$', views.DisplayChart, name = 'google-chart'),
    url(r'^seat-booking/$', views.Seat_Booking, name = 'seat-booking'),
    url(r'^movie-list/$', views.Movie_List, name = "movie-list"),
    url(r'^booking-create/$', views.booking_create, name='booking-create'),
    url(r'^movie-list-detail/(?P<pk>\d+)/$', Movie_DetailView.as_view(), name='movie-list-detail'),
    url(r'^user-booking/$', UserBookings.as_view(), name = "user-booking"),


]