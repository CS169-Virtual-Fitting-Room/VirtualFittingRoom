from django.db import models
from time import datatime
class User (models.Model):
	name = models.CharField(max_length = 128, primary_key = True)
	##password = models.CharField(max_length = 128)
	count = models.IntegerField(default = 0)
	signUpTime = models.DataField()
	lastLogInTime = models.DateField()
	userImage = models.CharField(max_length = 128)
	def __unicode__(self):
	    return self.name

class WishList(models.Model):
	owner = models.OneToOneField(User, primary_key = True)

	product = models.CharField(max_length = 128)
	#createTime = models.DateField()


class Product(models.Model):
	owner = models.ForeignKey(User)  
	category = models.ForeignKey(Category)
	wishList = models.ForeignKey(WishList)

	name = models.CharField(max_length = 128, primary_key = True)
	brand = models.CharField(max_length = 128)
	url = models.CharField(max_length = 128)
	timeAdded = models.DataField()

	photo = models.CharField(max_length = 128)
	def __unicode__(self):
	    return self.name
	    
class Comment(models.Model):
	owner = models.ForeignKey(User)
	productCommented = models.ForeignKey(Product)

	content = models.CharField(max_length = 128)
	##timeAdded = models.DataField()


class Category(models.Model):
	name = models.CharField(max_length = 128, primary_key = True)
	photo = models.CharField(max_length = 128)

	def __unicode__(self):
	    return self.name
# Create your models here.
