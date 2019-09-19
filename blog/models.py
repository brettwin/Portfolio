from django.db import models

# Create your models here.
#create a blog models
#add blog app to settings
    # Title
    # pub date
    # body
    # image

#create migration
#migrate
#add to admin


class Blog(models.Model):
    Title = models.CharField("Title", max_length=255)
    Publication_Date = models.DateTimeField()
    Body = models.TextField()
    image = models.ImageField(upload_to='images/')
