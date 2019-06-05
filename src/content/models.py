from django.db import models

# Create your models here.
class Ingredients(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title 


class DishType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Dishes(models.Model):
    picture_dish = models.ImageField()
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    ingredients = models.ManyToManyField(Ingredients)
    featured = models.BooleanField(default=False)
    dish_type = models.ManyToManyField(DishType)

    def __str__(self):
        return self.title



class GalleryCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    item = models.ImageField()
    name = models.CharField(max_length=100, blank=True, null=True)
    categories = models.ManyToManyField(GalleryCategory)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name



class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name