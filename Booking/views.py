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

def Movie_List(request):
    context = {}
    movie_name = request.POST.get('movies_filter')
    if movie_name is None:
        context["movie_list"] = Movie.objects.all()
    else:
        context["movie_list"] = Movie.objects.filter(movie_name__icontains = movie_name)
    context["movie_list_all"] = Movie.objects.all()
    return render(request, "Booking/index.html", {"context": context})

# ----------------------------------------------------------------------------------------------------------------------

def booking_create(request):
    seat_list = request.POST.getlist('seat_list[]')
    theater_id = request.POST.get('theater_id')
    movie_id = request.POST.get('movie_id')
    show_id = request.POST.get('show_id')
    date_id = request.POST.get('date_id')
    booking_list = Screen_Select.objects.all()

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
        context = super(Movie_DetailView, self).get_context_data(*args, **kwargs)
        movie_name = self.get_object()
        date = self.request.GET.get("date_screen")
        if date is not None:
            context['Screen_Select'] = Screen_Select.objects.filter(movie_screen_id=movie_name,
                                                                    date_screen_id = date)

        else:
            context['Screen_Select'] = Screen_Select.objects.filter(movie_screen_id = movie_name,
                                                                    date_screen_id=1).order_by('date_screen_id')

        context['movie_id'] = movie_name
        # context['movie_img'] = Screen_Select.objects.filter(movie_screen_id=movie_name).distinct('pk')
        context['Theater'] = Screen_Select.objects.all().distinct('theater_screen_id').order_by('theater_screen_id')
        context['Date'] = Screen_Select.objects.all().distinct('date_screen_id').order_by('date_screen_id')
        context['show'] = Show.objects.all()
        context['date_id'] = date
        return context

# ----------------------------------------------------------------------------------------------------------------------

def Seat_Booking(request):
    list_seat = []
    context = {}
    theater = request.POST.get("theater_screen")
    movie = request.POST.get("movie_screen")
    show = request.POST.get("show_screen")
    date = request.POST.get("date_screen")
    # print theater
    # print movie
    # print show
    # print date
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
    if request.is_ajax():
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
    else:
        return render(request, "Booking/booking_status.html")


def Seat_Booked(request):
    list_seat = []
    theater_id = request.POST.get('theater_id')
    movie_id = request.POST.get('movie_id')
    show_id = request.POST.get('show_id')
    date_id = request.POST.get('date_id')
    booking = Booking.objects.filter(theater_id = theater_id,
                                     movie_id = movie_id,
                                     show_id = show_id,
                                     date_id =date_id)
    for i in booking:
        list_seat.append(i.seat);
    return HttpResponse(json.dumps(list_seat), content_type="application/json")

class UserBookings(LoginRequiredMixin, ListView):
    template_name = 'Booking/user_booking.html'
    paginate_by = 10
    def get_queryset(self):

        queryset = Booking.objects.filter(user = self.request.user)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(UserBookings, self).get_context_data(*args, **kwargs)
        queryset = Booking.objects.filter(user=self.request.user)
        context["theater_list"] = queryset.values('theater_id', "theater_id__theater_name").distinct()
        # print context['theater_list']
        context['movie_list'] = queryset.values('movie_id', 'movie_id__movie_name').distinct()
        context['show_list'] = queryset.values('show_id', 'show_id__show').distinct()
        context['date_list'] = queryset.values('date_id', 'date_id__date').distinct()
        return context