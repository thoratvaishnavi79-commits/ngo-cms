from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='banners/')

    def __str__(self):
        return self.title
