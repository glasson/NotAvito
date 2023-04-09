from django.db import models



class Category(models.Model):
    categoryName = models.CharField(max_length=30)


class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=512)
    photo = models.URLField()
    owner = models.ForeignKey('auth.user',on_delete=models.DO_NOTHING)
    contacts = models.CharField(max_length=15)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    price = models.IntegerField()
    publicationDate = models.DateTimeField()
    rating = models.FloatField()
# Create your models here.
