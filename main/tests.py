from django.test import TestCase
from dataBaseModel import dataBaseModel
from main.models import Product
from main.models import Category
from main.models import Comment
from main.models import User
from main.models import WishList
from django.contrib.auth.models import User as AUser

###    Create your tests here.

###    google account: fittingroomtem@gmail.com
###    password : berkeleycs169

class testUnit(TestCase):
    SUCCESS = 1
    ERR_BAD_PRODUCT = -1
    ERR_BAD_USER = -2
    ERR_UNABLE_TO_REMOVE_FROM_WISHLIST = -3
    ERR_BAD_CATEGORY = -4

    testUsersID = []
    testUsers = []
    testCategory = []
    testProducts = []
    testComments = []
    testWishLists = []
    def setUp(self):

###### create Users #######
        addUser = ["a", "b", "c", "d"]

        for i in range(4):
            auser = AUser(username = addUser[i], password = "berkeleycs169")
            auser.save()
            newUser = User(user = auser, user_image = "null")
            newUser.save()
            testUnit.testUsers.append(newUser)
            testUnit.testUsersID.append(newUser.pk)

######   add Category ######
        category1 = Category(name = "hat")
        testUnit.testCategory.append(category1)
        category1.save()


######   add product ######
        addProducts = ["aaaa","bbbb","cccc","dddd"]
        for i in range(4):  ## add products
            newOne = Product(category = category1, name = addProducts[i], brand = "null", \
                             url = "null", photo = "null", price = 1.0 )
            newOne.save()
            testUnit.testProducts.append(newOne)

##### ## add comments   ######
        for i in range(4):
            newOne = Comment(product = testUnit.testProducts[i], owner = testUnit.testUsers[i], content = "null")
            newOne.save()
            testUnit.testComments.append(newOne)


######  add wishList   ######
        for i in range(4):
            newOne = WishList(owner = testUnit.testUsers[i], product = testUnit.testProducts[i])
            newOne.save()
            testUnit.testWishLists.append(newOne)



    def testGetProduct(self):
        baseModel = dataBaseModel()
        products = baseModel.getProducts(testUnit.testCategory[0])
        for i in range(4):
            self.assertTrue(testUnit.testProducts[i] in products[0] and products[1] == testUnit.SUCCESS, "addProduct failed")
        self.assertTrue("eeee" not in products[0], "addProduct failed")


    def testGetDetail(self):
        baseModel = dataBaseModel()
        for i in range(4):
            productDetail = baseModel.getDetail(testUnit.testProducts[i])
            self.assertTrue(productDetail != None, "getDetail failed, can not find the product")
            self.assertTrue(productDetail[0].category == testUnit.testCategory[0], "getDetail failed, wrong category")
            self.assertTrue(productDetail[0].brand == "null", "getDetail failed, wrong brand")
            self.assertTrue(productDetail[0].url == "null", "getDetail failed, wrong url")
            self.assertTrue(productDetail[0].photo == "null", "getDetail failed, wrong photo")
            self.assertTrue(productDetail[0].price == 1.0, "getDetail failed, wrong price")
        productDetail = baseModel.getDetail("eeee")
        self.assertTrue(productDetail[0] == None, "getDetail failed, can not detect non exist product")


    def testAddToWishList(self):
        baseModel = dataBaseModel()
        for i in range(4):
            response = baseModel.addToWishList(testUnit.testUsersID[i], testUnit.testProducts[i])
            self.assertTrue(response == testUnit.SUCCESS, "addToWishList failed, can not add")


    def testRemoveFromWishList(self):
        baseModel = dataBaseModel()
        for i in range(4):
            response = baseModel.removeFromWishList(testUnit.testUsers[i], testUnit.testProducts[i])
            self.assertTrue(response == testUnit.SUCCESS, "can not do removeFromWishList")

        response = baseModel.removeFromWishList(testUnit.testUsers[0], "eeee")
        self.assertTrue(response == testUnit.ERR_UNABLE_TO_REMOVE_FROM_WISHLIST, "remove non-exist product  fails")

        response = baseModel.removeFromWishList("a", testUnit.testProducts[0])
        self.assertTrue(response == testUnit.ERR_UNABLE_TO_REMOVE_FROM_WISHLIST, "remove non-exist product  fails")


    def testGetWishList(self):
        baseModel = dataBaseModel()
        for i in range(4):
            response = baseModel.getWishList(testUnit.testUsersID[i])
            self.assertTrue(response == testUnit.SUCCESS, "can not get WishList")

        response = baseModel.getWishList(6)  ## "e" user does not exist
        self.assertTrue(response == testUnit.ERR_BAD_USER, "get wishList from non exist user")



    def testAddComment(self):
        baseModel = dataBaseModel()
        for i in range(4):
            response = baseModel.addComment(testUnit.testUsersID[i], testUnit.testProducts[i], "this is comment from user " + str(i))
            self.assertTrue(response == testUnit.SUCCESS, "add comment not success")

        response = baseModel.addComment(testUnit.testUsersID[0], "eeee", "this is comment from user non exist")
        self.assertTrue(response == testUnit.ERR_BAD_PRODUCT, " add comment to non exist product")

        response = baseModel.addComment(6, testUnit.testProducts[0], "this is comment from user e" )
        self.assertTrue(response == testUnit.ERR_BAD_USER, "add comment to non-exist user")



    def testGetComment(self):
        baseModel = dataBaseModel()
        for i in range(4):
            temp = testUnit.testComments[i]
            response = baseModel.getComment(testUnit.testProducts[i])
            self.assertTrue(temp in response[0] and response[1] == testUnit.SUCCESS, " can not find the comment")

        response = baseModel.getComment("eeee") # product not exist
        self.assertTrue(response[0] == [] and response[1] == testUnit.ERR_BAD_PRODUCT, "get comment from a non exist product")

