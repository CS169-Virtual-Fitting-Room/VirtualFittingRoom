"""
1)
the validation case needs to be more informative..probably add more err code
eg. badUserID, badProductID

2)
also for a ForeignKey field, you need to actually add a reference model to it
eg. 
class Comment:
    owner = ForeignKey(User)
    ...

to add a new comment, you need
newComment = Comment()
newComment.owner = User.objects.get(id = uid)
newComment.save()

3) we just store a directory of the image in our user table, so when adding an image, we need a new "ImageWriter" class
to write the image to filesystem. Then here we just insert the URI to it

4) removeProduct
don't we just get a productID and remove it?
Product.objects.get(id = pid).delete()
"""

# This class encapsulates all communication with the DB
from models import User
from models import Comment
from models import Product
from models import Category
from models import WishList

from django.db.models import Q

class dataBaseModel (object):
    
    SUCCESS = 1
    ERR_BAD_CREDENTIALS = -1
    ERR_USER_EXISTS = -2
    ERR_BAD_USERNAME = -3
    ERR_BAD_PASSWORD = -4
    Err_Num = -1
    Good_Num = 1
    MAX_USERNAME_LENGTH = 128
    MAX_PASSWORD_LENGTH = 128

    ERR_BAD_OTHERS = -5
    
    def __init__(self):
        # do nothing
        pass
    """    
    Sth Idk how to do
    def addUserPhoto(self, userName, Photo):
        if userName is None:
            return (dataBaseModel.ERR_BAD_USERNAME, self.Err_Num)
        if Photo is None:
            return (dataBaseModel.ERR_BAD_OTHERS, self.Err_Num) 
        try{
            newOne = User.objects.get(Q(name = userName),)
    """                
    def addToWishList(self, userID, productID): # eddie: use ID instead of name
        '''
        if userID is None or (userName) > dataBaseModel.MAX_USERNAME_LENGTH or len(userName) == 0 :
            return (dataBaseModel.ERR_BAD_USERNAME, self.Err_Num)
        if productName is None :
            return (dataBaseModel.ERR_BAD_OTHERS, self.Err_Num)
        '''
        
        '''
        no need to query from db, we are adding a new row
        newOne = WishList.objects.get(Q(owner = userName))        
        newOne.add(productName)
        '''
        
        newOne = WishList(owner = User.objects.get(id = userID), product = Product.objects.get(id = productID))
        newOne.save()
        return (dataBaseModel.SUCCESS, "add to wishList successfully")


    def removeFromWishList(self, userID, productID): # use id as above
        """
        if userName is None or (userName) > dataBaseModel.MAX_USERNAME_LENGTH or len(userName) == 0 :
            return (dataBaseModel.ERR_BAD_USERNAME, self.Err_Num)
        if productName is None:
            return (dataBaseModel.ERR_BAD_OTHERS, self.Err_Num)
        """
        newOne = WishList.objects.get(Q(owner = User.objects.get(id = userID)), Q(product = User.objects.get(id = productID)))
        """
        use delete() instead
        newOne.remove(productName)
        newOne.save()
        """
        newOne.delete()
        return (dataBaseModel.SUCCESS, "remove from wishList successfully")

    def getWishList(self, userID): # ID
        """
        we have multiple rows for one userID, we need a queryset
        
        if userName is None or (userName) > dataBaseModel.MAX_USERNAME_LENGTH or len(userName) == 0 :
            return (dataBaseModel.ERR_BAD_USERNAME, self.Err_Num)
        newOne = WishList.objects.get(Q(owner = userName)) 
        """
        items = []
        for item in WishList.objects.filter(owner = User.objects.get(id = userID)):
            items.append(item.product) # we now only obtain the product model..may be we want some specific field from the table
        
        return (items, dataBaseModel.SUCCESS, "get wishList successfully")


    def addComment(self, userID, productID, content): # ID
        """
        if userName is None or (userName) > dataBaseModel.MAX_USERNAME_LENGTH or len(userName) == 0 :
            return (dataBaseModel.ERR_BAD_USERNAME, self.Err_Num)
        if productName is None :
            return (dataBaseModel.ERR_BAD_OTHERS, self.Err_Num)

        if len(content) > dataBaseModel.MAX_PASSWORD_LENGTH: # check if password is valid
            return (dataBaseModel.ERR_BAD_OTHERS, self.Err_Num)
        """

        newOne = Comment(owner = User.objects.get(id = userID), product = Product.objects.get(id = productID), content)
        newOne.save()
        return (dataBaseModel.SUCCESS, "comment added successfully")


    def getComment(self, productID): # here we just want to retreive a list of comments on that product
        """
        if userName is None or (userName) > dataBaseModel.MAX_USERNAME_LENGTH or len(userName) == 0 :
            return (dataBaseModel.ERR_BAD_USERNAME, self.Err_Num)
        if productName is None :
            return (dataBaseModel.ERR_BAD_OTHERS, self.Err_Num)
        """
        items = []
        for item in Comment.objects.filter(product = Product.objects.get(id = productID)):
            items.append(item.content)
        
        return (items, dataBaseModel.SUCCESS, "comment shown")


    def getProducts(self, categoryID): # ID

        if categoryID is None:
            return (dataBaseModel.ERR_BAD_OTHERS, self.Err_Num)
        # here you simply get the category, instead of products
        #newOne = Category.objects.get(Q(name = categoryName))
        items = []
        for item in Product.objects.filter(category = Category.objects.get(id = categoryID)):
            items.append(item) # here we just append the item model, should add some specfici fields
        return (items, dataBaseModel.SUCCESS, "products list")
    
    
"""  sth idk how to do
    def removeProduct(userName, productName):
        if userName is None or (userName) > dataBaseModel.MAX_USERNAME_LENGTH or len(userName) == 0 :
            return (dataBaseModel.ERR_BAD_USERNAME, self.Err_Num)
        if productName is None 
            return (dataBaseModel.ERR_BAD_OTHERS, self.Err_Num)
        newOne = Product.objects.get(Q(owner = userName))     
"""   
