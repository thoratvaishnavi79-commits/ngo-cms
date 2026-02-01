from django.db import models
from django.utils.text import slugify

# OUR STORY
class OurStory(models.Model):
    content = models.TextField()

    def __str__(self):
        return "Our Story"


# CORE VALUES
class CoreValue(models.Model):
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value


# PROGRAMS

class Program(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(default="")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# TEAM MEMBERS
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')

    def __str__(self):
        return self.name
