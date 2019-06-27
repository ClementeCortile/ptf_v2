from django.db import models


class Projects(models.Model):
    title = models.CharField(max_length=200, default="")
    image = models.ImageField(upload_to='images/')
    image_details = models.ImageField(upload_to='images/', blank=True, null=True)
    summary = models.TextField(max_length=200, default="")
    title_video = models.CharField(max_length=200, default="", blank=True, null=True)
    video = models.URLField(max_length=250, blank=True, null=True)
    title_link = models.CharField(max_length=200, default="", blank=True, null=True)
    link = models.URLField(max_length=250, blank=True, null=True)
