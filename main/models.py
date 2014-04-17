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
    overlay = models.CharField(max_length = 256)
    price = models.FloatField()
    description = models.CharField(max_length = 256)
    def __unicode__(self):
        return self.name

class WishList(models.Model):
    #owner = models.OneToOneField(User, primary_key = True)
    owner = models.ForeignKey(AUser)
    product = models.ForeignKey(Product)
    #create_time = models.DateField()
    
    class meta:
        unique_together = ('owner', 'product')
        
    def __unicode__(self):
        return str(self.owner) + str(self.product)
    
class FitList(models.Model):
    #owner = models.OneToOneField(User, primary_key = True)
    owner = models.ForeignKey(AUser)
    product = models.ForeignKey(Product)
    #create_time = models.DateField()
    
    class meta:
        unique_together = ('owner', 'product')
        
    def __unicode__(self):
        return str(self.owner) + str(self.product)
    
class TempProduct(models.Model):
    owner = models.ForeignKey(AUser)
    #name = models.CharField(max_length = 128)
    overlay = models.CharField(max_length = 256)
    token = models.CharField(max_length = 256)
    category = models.ForeignKey(Category)
    #create_time = models.DateField()
    
    class meta:
        unique_together = ('owner', 'product')
        
    def __unicode__(self):
        return str(self.owner) + str(self.product)

class Comment(models.Model):
    product = models.ForeignKey(Product)
    owner = models.ForeignKey(AUser)
    time = models.DateTimeField()
    content = models.CharField(max_length = 256)
    #time_added = models.DateTimeField()
    
class Added(models.Model):
    owner = models.ForeignKey(AUser)
    product = models.ForeignKey(Product)
    
    def __unicode__(self):
        return str(self.owner) + str(self.product)
