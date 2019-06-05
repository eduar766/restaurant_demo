from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from tinymce import HTMLField

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()
    phrase = models.CharField(max_length=300)
    facebook = models.URLField()
    twitter = models.URLField()
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Categories(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Tags(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=150)
    thumbnail = models.ImageField()
    pub_date = models.DateTimeField(auto_now_add=True)
    is_video = models.BooleanField(default=False)
    video_url = models.URLField(max_length=200, blank=True)
    category = models.ManyToManyField(Categories)
    tag = models.ManyToManyField(Tags)
    like = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = HTMLField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={
            'id': self.id
        })

    @property
    def get_comments(self):
        return self.comments.all().order_by('-pub_date_comment')


class Comment(models.Model):
    person = models.CharField(max_length=150)
    pub_date_comment = models.DateField(auto_now_add=True)
    email = models.EmailField()
    content = models.TextField()
    post = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return self.person