from django.db import models

# Create your models here.
class Team(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    
    facebook_link = models.URLField(max_length=200, blank=True)
    twitter_link = models.URLField(max_length=200, blank=True)
    google_plus_link = models.URLField(max_length=200, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

