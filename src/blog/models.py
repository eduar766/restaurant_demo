from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    thumbnail = models.ImageField()
    pub_date = models.DateTimeField(auto_now_add=True)
    is_video = models.BooleanField(default=False)
    video_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title
