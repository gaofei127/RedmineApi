from django.db import models

# Create your models here.

class People(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
    job = models.CharField(null=True, blank=True, max_length=200)
    def __str__(self):
        return self.name

class Ariticle(models.Model):
    headline = models.CharField(null=True, blank=True, max_length=500)
    content = models.TextField(null=True, blank=True)
    TAG_CHOICE = (
        ('tech', 'Tech'),
        ('life', 'Life')
    )
    tag = models.CharField(null=True, blank=True, max_length=500, choices=TAG_CHOICE)
    def __str__(self):
        return self.headline

class Comment(models.Model):
    name = models.CharField(null=True, blank=True, max_length=50)
    comment = models.TextField()
    def __str__(self):
        return self.comment


