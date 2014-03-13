from django.db import models
from django.contrib.auth.models import User as AUser

class User (models.Model):
    user = models.OneToOneField(AUser) 
    count = models.IntegerField(default = 0)
    user_image = models.CharField(max_length = 256)
    def __unicode__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length = 256)

    def __unicode__(self):
        return self.name

class Product(models.Model):  
    category = models.ForeignKey(Category)
    #wishList = models.ForeignKey(WishList)
    name = models.CharField(max_length = 128)
    brand = models.CharField(max_length = 128)
    url = models.CharField(max_length = 256)
    photo = models.CharField(max_length = 256)
    price = models.FloatField()
    description = models.CharField(max_length = 256)
    def __unicode__(self):
        return self.name

class WishList(models.Model):
    #owner = models.OneToOneField(User, primary_key = True)
    owner = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    create_time = models.DateField()
    
    class meta:
        unique_together = ('owner', 'product')

class Comment(models.Model):
    product = models.ForeignKey(Product)
    owner = models.ForeignKey(User)

    content = models.CharField(max_length = 256)
    #time_added = models.DateTimeField()
