from django.test import TestCase
from dataBaseModel import dataBaseModel
from main.models import Product, Category, Comment, User, WishList,

###    Create your tests here.

###    google account: fittingroomtem@gmail.com
###    password : berkeleycs169

class testUnit(TestCase):
    SUCCESS = 1
    ERR_BAD_PRODUCT = -1
    ERR_BAD_USER = -2
    ERR_UNABLE_TO_REMOVE_FROM_WISHLIST = -3
    ERR_BAD_CATEGORY = -4


    testProducts = ["aaaa","bbbb","cccc","dddd"]
    testUsers = ["a", "b", "c", "d"]
    testCategory = ["hat"]

    def setUp(self):
        for i in range(4):  ## add users
            newOne = User(user = testUnit.testUsers[i], user_image = "null")
            newOne.save()

        for i in range(4):  ## add products
            newOne = Product(category = "hats", name = testUnit.testProducts[i], brand = "null", \
                             url = "null", photo = "null", price = 1.0 )
            newOne.save()
        for i in range(4):  ## add comments
            newOne = Comment(product = testUnit.testProducts[i], owner = testUnit.testUsers[i], content = "null")
            newOne.save()


    def testGetProduct(self):
        baseModel = dataBaseModel()
        products = baseModel.getProducts("hats")
        for i in range(4):
            self.assertTrue(testUnit.testProducts[i] in products[0] and products[1] == testUnit.SUCCESS, "addProduct failed")
        self.assertTrue("eeee" not in products[0], "addProduct failed")


    def testGetDetail(self):
        baseModel = dataBaseModel()
        for i in range(4):
            productDetail = baseModel.getDetail(testUnit.testProducts[i])
            self.assertTrue(productDetail != None, "getDetail failed, can not find the product")
            self.assertTrue(productDetail.category == "hats", "getDetail failed, wrong category")
            self.assertTrue(productDetail.brand == "null", "getDetail failed, wrong brand")
            self.assertTrue(productDetail.url == "null", "getDetail failed, wrong url")
            self.assertTrue(productDetail.photo == "null", "getDetail failed, wrong photo")
            self.assertTrue(productDetail.price == 1.0, "getDetail failed, wrong price")
        productDetail = baseModel.getDetail("eeee")
        self.assertTrue(productDetail == None, "getDetail failed, false product")


    def testAddToWishList(self):
        baseModel = dataBaseModel()
        for i in range(4):
            response = baseModel.addToWishList(testUnit.testUsers[i], testUnit.testProducts[i])
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
            response = baseModel.getWishList(testUnit.testUsers[i])
            self.assertTrue(response == testUnit.SUCCESS, "can not do removeFromWishList")

        response = baseModel.getWishList("e")  ## "e" user does not exist
        self.assertTrue(response == testUnit.SUCCESS, "can not do getWishList")

    def testAddComment(self):
        baseModel = dataBaseModel()
        for i in range(4):
            response = baseModel.addComment(testUnit.testUsers[i], testUnit.testProducts[i], "this is comment from user " + i)
            self.assertTrue(response == testUnit.SUCCESS)

        response = baseModel.addComment(testUnit.testUsers[0], "eeee", "this is comment from user " + str(i))
        self.assertTrue(response == testUnit.ERR_BAD_PRODUCT)

        response = baseModel.addComment("e", testUnit.testProducts[0], "this is comment from user e" )
        self.assertTrue(response == testUnit.ERR_BAD_USER)

    def testGetComment(self):
        baseModel = dataBaseModel()
        for i in range(4):
            temp = "this is comment from user " + str(i)
            response = baseModel.getComment(testUnit.testProducts[i])
            self.assertTrue(temp in response[0] and response[1] == testUnit.SUCCESS)

        response = baseModel.getComment("eeee") # product not exist
        self.assertTrue(response[0] == [] and response[1] == testUnit.ERR_BAD_PRODUCT)






