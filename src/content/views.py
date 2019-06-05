from django.shortcuts import render, get_object_or_404
from .models import Ingredients, Dishes, DishType, Gallery, Reservation, ContactForm
from blog.models import *
from django.db.models import Count, Q
from .search_db import *


def index(request):
    gallery = Gallery.objects.all()
    blogs = Blog.objects.all().order_by('-pub_date')[0:3]

    if request.method == 'POST':
        full_name = request.POST['full-name']
        email = request.POST['email']
        phone = request.POST['phone']
        new_reservation = Reservation()
        new_reservation.full_name = full_name
        new_reservation.email = email
        new_reservation.phone = phone
        new_reservation.save()


    context = {
        'count': count,
        'count_all': count_all,
        'blogs': blogs,

        'allDishes': query,
        'breakfast': breakfast,
        'count_breakfast': count_breakfast,
        'lunch': lunch,
        'count_lunch': count_lunch,
        'dinner': dinner,
        'count_dinner': count_dinner,
        'drink': drink,
        'count_drink': count_drink,
        'party': party,
        'count_party': count_party,
        'coffee': coffee,
        'count_coffee': count_coffee,

        'gallery': gallery,
    }

    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about-us.html')


def menu(request):
    context = {
        'breakfast':breakfast,
        'lunch': lunch,
        'dinner': dinner,
        'dessert': dessert,
        'coffee': coffee,
        'juice':juice,
        'soft':soft,
        'hard':hard,
        'query': query
    }
    return render(request, 'food-menu.html', context)


def gallery(request):
    gallery = Gallery.objects.all()
    context = {
        'gallery': gallery,
    }
    return render(request, 'gallery.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        new_contact = ContactForm()
        new_contact.name = name
        new_contact.email = email
        new_contact.message = message
        new_contact.save()
    return render(request, 'contact-us.html')
