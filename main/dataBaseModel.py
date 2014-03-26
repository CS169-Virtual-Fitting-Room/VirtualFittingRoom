# This class encapsulates all communication with the DB
#from models import User
from django.contrib.auth.models import User
from models import Comment
from models import Product
from models import Category
from models import WishList
from models import FitList

from django.db.models import Q

class dataBaseModel (object):
    
    SUCCESS = 1
    ERR_BAD_PRODUCT = -1
    ERR_BAD_USER = -2
    ERR_UNABLE_TO_REMOVE_FROM_WISHLIST = -3
    ERR_UNABLE_TO_REMOVE_FROM_FITLIST = -4
    ERR_BAD_CATEGORY = -5
    ERR_WISHLIST_ALREADY_EXIST = -6
    ERR_FITLIST_ALREADY_EXIST = -7
    ERR_BAD_REQUEST = -8

    
    
    def __init__(self):
        # do nothing
        pass
            
    def addToWishList(self, userID, product, productID): 
        try:
            user = User.objects.get(pk = userID)
            p = Product.objects.get(Q(pk = productID), Q(name = product))
            if WishList.objects.filter(Q(owner = user), Q(product = p)).count() != 0: #check if item already exist
                return dataBaseModel.ERR_WISHLIST_ALREADY_EXIST
        
            newOne = WishList(owner = user, product = p) # create a new wishlist item
            newOne.save()
            return dataBaseModel.SUCCESS
        except:
            return dataBaseModel.ERR_BAD_PRODUCT


    def removeFromWishList(self, userID, product, productID):
        try:
            #try to get the wishlist item
            newOne = WishList.objects.get(Q(owner = User.objects.get(pk = userID)), Q(product = Product.objects.get(Q(pk = productID), Q(name=product))))
        except:
            return dataBaseModel.ERR_UNABLE_TO_REMOVE_FROM_WISHLIST
        newOne.delete() # delete the item
        return dataBaseModel.SUCCESS

    def getWishList(self, userID):
        try:
            User.objects.get(pk = userID)
        except:
            return ([], dataBaseModel.ERR_BAD_USER)
        
        queryset = WishList.objects.filter(owner = User.objects.get(pk = userID)) # query the wishlist of the user 
        items = []
        for item in queryset:
            items.append(item)

        return (items, dataBaseModel.SUCCESS)
    
    """ fitlist operation is very similar to wishlist...may consider refactor? """
    
    def addToFitList(self, userID, product, productID): 
        try:
            user = User.objects.get(pk = userID)
            p = Product.objects.get(Q(pk = productID), Q(name = product))
            if FitList.objects.filter(Q(owner = user), Q(product = p)).count() != 0: #check if item already exist
                return dataBaseModel.ERR_FITLIST_ALREADY_EXIST
        
            newOne = FitList(owner = user, product = p) # create a new fitlist item
            newOne.save()
            return dataBaseModel.SUCCESS
        except:
            return dataBaseModel.ERR_BAD_PRODUCT


    def removeFromFitList(self, userID, product, productID):
        try:
            #try to get the fitlist item
            newOne = FitList.objects.get(Q(owner = User.objects.get(pk = userID)), Q(product = Product.objects.get(Q(pk = productID), Q(name=product))))
        except:
            return dataBaseModel.ERR_UNABLE_TO_REMOVE_FROM_FITLIST
        newOne.delete() # delete the item
        return dataBaseModel.SUCCESS

    def getFitList(self, userID):
        try:
            User.objects.get(pk = userID)
        except:
            return ([], dataBaseModel.ERR_BAD_USER)
        
        queryset = FitList.objects.filter(owner = User.objects.get(pk = userID)) # query the fitlist of the user 
        items = []
        for item in queryset:
            items.append(item)

        return (items, dataBaseModel.SUCCESS)


    def addComment(self, userID, product, pid, content, time):
        try:
            user = User.objects.get(pk=userID)
            p = Product.objects.get(Q(pk=pid), Q(name=product))
            newOne = Comment(owner = user, product = p, content = content, time=time)
            newOne.save()
            return dataBaseModel.SUCCESS
        except:
            return dataBaseModel.ERR_BAD_PRODUCT


    def getComments(self, product, pid):
        try :
            p = Product.objects.get(Q(pk = pid), Q(name=product))
                
            
            items = []
            for item in Comment.objects.filter(product = p).order_by('time'):
                items.append(item)
            
            return (items, dataBaseModel.SUCCESS)
        except:
            return ([], dataBaseModel.ERR_BAD_PRODUCT) 


    def getProducts(self, category):
        queryset = Product.objects.filter(category = Category.objects.filter(name = category))
        if queryset.count() == 0:
            return ([], dataBaseModel.ERR_BAD_CATEGORY)

        items = []
        for item in queryset:
            items.append(item)
            
        return (items, dataBaseModel.SUCCESS)
    
    def getDetail(self, product, productID):
        try:
            return (Product.objects.get(Q(pk=productID), Q(name=product)), dataBaseModel.SUCCESS)
        except:
            return (None,dataBaseModel.ERR_BAD_PRODUCT) 
