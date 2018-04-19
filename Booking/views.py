from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from datetime import datetime
from django.core import serializers
import json
from datetime import date

class HomeView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('/movie-list')
        else:
            return redirect('/register')

# ----------------------------------------------------------------------------------------------------------------------

def register(request):
    print request.method
    username = request.POST.get('username')
    email =  request.POST.get('email')
    password =  request.POST.get('password')
    if not (username == "" or username is None or email == "" or email is None or password == "" or password is None):
        if not(User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
            User.objects.create_user(username, email, password)
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('/movie-list')
        else:
            error = "Looks like a username with that email or password already exists"
            return render(request, 'registration/register.html', {'error': error})
    else:
        return render(request, 'registration/register.html')

# ----------------------------------------------------------------------------------------------------------------------

class Booking_ListView(LoginRequiredMixin, ListView):
    template_name = 'Booking/index.html'
    paginate_by = 10
    def get_queryset(self):
        theater_id_1 = self.request.GET.get('theater_id_1')
        movie_id_1 = self.request.GET.get('movie_id_1')
        show_id_1 = self.request.GET.get('show_id_1')
        date_id_1 = self.request.GET.get('date_id_1')
        booking_list_1 = Screen_Select.objects.all()

        if theater_id_1 is not None and theater_id_1 != "":
            booking_list_1 = booking_list_1.filter(theater_screen_id=theater_id_1)

        if movie_id_1 is not None and movie_id_1 != "":
            booking_list_1 = booking_list_1.filter(movie_screen_id=movie_id_1)

        if show_id_1 is not None and show_id_1 != "":
            booking_list_1 = booking_list_1.filter(show_screen_id=show_id_1)

        if date_id_1 is not None and date_id_1 != "":
            date_check = datetime.strptime(date_id_1, '%Y-%m-%d').date()
            booking_list_1 = booking_list_1.filter(date=date_check)

        if booking_list_1:
            return booking_list_1
        else:
            queryset = Screen_Select.objects.all()
            return queryset

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['theatre'] = Theater.objects.all()
        context['movie'] = Movie.objects.all()
        context['show'] = Show.objects.all()

        # And so on for more models
        return context
# ----------------------------------------------------------------------------------------------------------------------

def booking_create(request):
    seat_list = request.POST.getlist('seat_list[]')
    theater_id = request.POST.get('theater_id')
    movie_id = request.POST.get('movie_id')
    show_id = request.POST.get('show_id')
    date_id = request.POST.get('date_id')
    booking_list = Screen_Select.objects.all()
    print seat_list
    print theater_id
    print movie_id
    print show_id
    print date_id

    if theater_id is not None and theater_id != "":
        booking_list = booking_list.filter(theater_screen_id=theater_id)

    if movie_id is not None and movie_id != "":
        booking_list = booking_list.filter(movie_screen_id=movie_id)

    if show_id is not None and show_id != "":
        booking_list = booking_list.filter(show_screen_id=show_id)

    if date_id is not None and date_id != "":
        booking_list = booking_list.filter(date_screen_id=date_id)

    if booking_list:
        for screen in booking_list:
            screen_check = screen.screen_id_id
        for i in range(len(seat_list)):
            Booking_Ticket = Booking.objects.filter(theater_id=theater_id,
                                                    movie_id=movie_id,
                                                    show_id=show_id,
                                                    date_id=date_id)

        for i in range(len(seat_list)):
            Booking_Ticket = Booking.objects.filter(theater_id=theater_id,
                                                    movie_id=movie_id,
                                                    show_id=show_id,
                                                    date_id=date_id)

            booking_created = Booking.objects.create(user=request.user,
                                                     theater_id_id=theater_id,
                                                     movie_id_id=movie_id,
                                                     show_id_id=show_id,
                                                     screen_id_id=screen_check,
                                                     seat=seat_list[i],
                                                     date_id_id=date_id
                                                     )
        return HttpResponse(json.dumps(seat_list), content_type="application/json")
    else:
        error_message = "Please enter proper details"
        return render(request, "Booking/booking_confirmed.html", {'error_message': error_message})
# ----------------------------------------------------------------------------------------------------------------------

class Movie_DetailView(LoginRequiredMixin, DetailView):
    template_name = 'Booking/booking_detail.html'
    model = Movie
    # queryset = Theater.objects.all()

    def get_context_data(self, *args, **kwargs):
        movie_name = self.get_object()
        context = super(Movie_DetailView, self).get_context_data(*args, **kwargs)
        context['Screen_Select'] = Screen_Select.objects.filter(movie_screen_id = movie_name)
        return context

# ----------------------------------------------------------------------------------------------------------------------

def Seat_Booking(request):
    list_seat = []
    context = {}
    theater = request.POST.get("theater_screen")
    movie = request.POST.get("movie_screen")
    show = request.POST.get("show_screen")
    date = request.POST.get("date_screen")
    booking = Booking.objects.filter(theater_id_id = theater,
                                     movie_id_id = movie,
                                     show_id_id = show,
                                     date_id_id = date)
    for i in booking:
        list_seat.append(i.seat)
    context["A"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    context["B"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    context["C"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    context["D"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    context["E"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    context["F"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    context["G"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    context["H"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    context["I"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    context["J"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


    return render(request, "Booking/seat_booking.html", {"context":context,
                                                         "list_seat":list_seat,
                                                         "theater_booking": theater,
                                                         "movie_booking": movie,
                                                         "show_booking": show,
                                                         "date_booking": date})


def DisplayChart(request):
    list_chart = []
    date_count = Date.objects.all()
    movie_count = Movie.objects.all()
    list_movie = ["Date"]

    for movie in movie_count:
        list_movie.append(movie.movie_name)
    list_chart.append(list_movie)

    for date in range(len(date_count)):
        counter = date+1
        booking_date_list = Booking.objects.all()
        date = booking_date_list.filter(date_id=date+1)
        movie_counter = 0
        list_date = []
        date_list = Date.objects.filter(pk=counter)

        for x in date_list:
            date_convert_string = x.date
            date_string = date_convert_string.strftime('%d/%m/%Y')
            list_date.append(date_string)

        for i in movie_count:
            movie_counter+=1
            movie_id = date.filter(movie_id=movie_counter).count()
            list_date.append(movie_id)

        list_chart.append(list_date)
    return HttpResponse(json.dumps(list_chart), content_type="application/json")


def Seat_Booked(request):
    list_seat = []
    booking = Booking.objects.all()
    for i in booking:
        list_seat.append(i.seat);
    return HttpResponse(json.dumps(list_seat), content_type="application/json")