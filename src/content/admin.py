from django.contrib import admin
from .models import Ingredients, Dishes, DishType, GalleryCategory, Gallery, Reservation, ContactForm


admin.site.register(
    {
        Ingredients, Dishes, DishType, GalleryCategory, Gallery, Reservation, ContactForm
    }
)
