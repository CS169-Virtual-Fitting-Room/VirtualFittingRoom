# This class encapsulates all communication with the DB
from logincount.models import User
from logincount.models import Comment
from logincount.models import product
from logincount.models import Category
from logincount.models import WishList

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
"""    Sth Idk how to do
    def addUserPhoto(self, userName, Photo):
        if userName is None:
            return (dataBaseModel.ERR_BAD_USERNAME, self.Err_Num)
        if Photo is None:
            return (dataBaseModel.ERR_BAD_OTHERS, self.Err_Num) 
        try{
            newOne = User.objects.get(Q(name = userName),)
"""                
    def addToWishList(self, userName, productName):
        if userName is None or (userName) > dataBaseModel.MAX_USERNAME_LENGTH or len(userName) == 0 :
            return (dataBaseModel.ERR_BAD_USERNAME, self.Err_Num)
        if productName is None 
            return (dataBaseModel.ERR_BAD_OTHERS, self.Err_Num)
        newOne = WishList.objects.get(Q(owner = userName))
        newOne.add(productName)
        newOne.save()
        return (dataBaseModel.SUCCESS, "add to wishList successfully")


    def removeFromWishList(self, userName, productName):
        if userName is None or (userName) > dataBaseModel.MAX_USERNAME_LENGTH or len(userName) == 0 :
            return (dataBaseModel.ERR_BAD_USERNAME, self.Err_Num)
        if productName is None
            return (dataBaseModel.ERR_BAD_OTHERS, self.Err_Num)
        newOne = WishList.objects.get(Q(owner = userName))
        newOne.remove(productName)
        newOne.save()
        return (dataBaseModel.SUCCESS, "add to wishList successfully")

    def getWishList(self, userName):
        if userName is None or (userName) > dataBaseModel.MAX_USERNAME_LENGTH or len(userName) == 0 :
            return (dataBaseModel.ERR_BAD_USERNAME, self.Err_Num)
        newOne = WishList.objects.get(Q(owner = userName)) 
        return (newOne, dataBaseModel.SUCCESS, "get wishList successfully")


    def addComment(self, userName, productName, content):
        if userName is None or (userName) > dataBaseModel.MAX_USERNAME_LENGTH or len(userName) == 0 :
            return (dataBaseModel.ERR_BAD_USERNAME, self.Err_Num)
        if productName is None 
            return (dataBaseModel.ERR_BAD_OTHERS, self.Err_Num)

        if len(content) > dataBaseModel.MAX_PASSWORD_LENGTH: # check if password is valid
            return (dataBaseModel.ERR_BAD_OTHERS, self.Err_Num)


        newOne = Comment(userName, productName, content)
        newOne.save()
        return (dataBaseModel.SUCCESS, "comment added successfully")


    def getComment(self, userName, productName):
        if userName is None or (userName) > dataBaseModel.MAX_USERNAME_LENGTH or len(userName) == 0 :
            return (dataBaseModel.ERR_BAD_USERNAME, self.Err_Num)
        if productName is None 
            return (dataBaseModel.ERR_BAD_OTHERS, self.Err_Num)

        newOne = Comment.objects.get(Q(owner = userName, productCommented = productName)
        return (newOne, dataBaseModel.SUCCESS, "comment shown")


    def getProducts(categoryName):
        if categoryName is None:
            return (dataBaseModel.ERR_BAD_OTHERS, self.Err_Num)
        newOne = Category.objects.get(Q(name = categoryName))
        return (newOne, dataBaseModel.SUCCESS, "products list")
"""  sth idk how to do
    def removeProduct(userName, productName):
        if userName is None or (userName) > dataBaseModel.MAX_USERNAME_LENGTH or len(userName) == 0 :
            return (dataBaseModel.ERR_BAD_USERNAME, self.Err_Num)
        if productName is None 
            return (dataBaseModel.ERR_BAD_OTHERS, self.Err_Num)
        newOne = Product.objects.get(Q(owner = userName))     
"""   
