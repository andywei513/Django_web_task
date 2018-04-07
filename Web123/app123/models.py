from django.db import models
from django.contrib import admin
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    body = models.TextField()
    create_date = models.DateTimeField()

    def __unicode__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username','password')

