from django.db import models


class Presentations(models.Model):
    image = models.ImageField(upload_to='images/', default='ptf_v2/static/No_image_3x4.svg.png')
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:10]
