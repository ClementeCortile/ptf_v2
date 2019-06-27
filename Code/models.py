from django.db import models


class Code(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    link = models.URLField(max_length=250, blank=True, null=True)
    body = models.TextField(max_length=2000, blank=True, null=True)
    image = models.ImageField(upload_to='images/', default='static/No_image_3x4.png')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:10]

