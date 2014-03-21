# don't change!
from main.models import User, Category, Product, WishList, FitList, Comment
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.models import User as AUser

def setUpDb(request):
    User.objects.all().delete()
    Category.objects.all().delete()
    Product.objects.all().delete()
    WishList.objects.all().delete()
    FitList.objects.all().delete()
    Comment.objects.all().delete()
    
    glasses = Category(name='glasses')
    hats = Category(name='hats')
    headphones = Category(name='headphones')
    glasses.save()
    hats.save()
    headphones.save()
    
    rayban = Product(category = glasses, name='rayban glasses', brand = 'rayban', url='www.rayban.com', photo='rayban.jpg', price = 129.9, description='stylish rayban')
    nike = Product(category = glasses, name='nike glasses', brand = 'nike', url='www.nike.com', photo='nike.jpg', price = 99.9, description = 'sporty nike')
    adidas = Product(category = hats, name='adidas cap', brand = 'adidas', url='www.adidas.com', photo='addidas.jpg', price = 56.9, description ='adidas cap!')
    levis = Product(category = hats, name='levis hat', brand = 'levis', url='www.levis.com', photo='levis.jpg', price = 67.9, description ='levis hat!')
    beats = Product(category = headphones, name='beats headphones', brand = 'beats', url='www.beats.com', photo='beats.jpg', price = 256.9, description='stylish headphones!')
    sony = Product(category = headphones, name='sony headphones', brand = 'sony', url='www.sony.com', photo='sony.jpg', price = 399.9, description='high quality headphones!')
    rayban.save()
    nike.save()
    adidas.save()
    levis.save()
    beats.save()
    sony.save()
    
    comment = Comment(product = rayban, owner = AUser.objects.get(pk=1), time=timezone.now(), content="Very nice glasses!")
    comment.save()
    
    wish = WishList(owner=AUser.objects.get(pk=1), product=rayban)
    wish.save()
    
    return HttpResponse("Success!")