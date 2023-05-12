# Create your models here.
from django.db import models


class Category(models.Model):
    categoryName = models.CharField(max_length=30)


class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=512)
    photo = models.ImageField(upload_to='media/img')
    owner = models.ForeignKey('auth.user', on_delete=models.DO_NOTHING, null=True)
    contacts = models.CharField(max_length=15, null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    price = models.IntegerField(null=True)
    publicationDate = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(null=True)
