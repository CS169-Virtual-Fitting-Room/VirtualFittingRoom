from django.test import TestCase
from dataBaseModel import dataBaseModel
from main.models import Product, Category, Comment, User, WishList,

# Create your tests here.

#google account: fittingroomtem@gmail.com
#password : berkeleycs169

class testUnit(TestCase):
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
    ERR_BAD_USERID = -10
    ERR_BAD_PRODUCTID = -11
    ERR_BAD_CATEGORYID = -12


    testProducts = ["aaaa","bbbb","cccc","dddd"]
    testUsers = ["a", "b", "c", "d"]
    testCategory = ["hat"]
    def setUp(self):
        for i in range(4):
            newOne = User(user = testUnit.testUsers[i], user_image = "null")
            newOne.save()

        for i in range(4):
            newOne = Product(category = "hats", name = testUnit.testProducts[i], brand = "null", \
                             url = "null", photo = "null", price = 1.0 )
            newOne.save()
        for i in range(4):
            newOne = Comment(product = testUnit.testProducts[i], owner = testUnit.testUsers[i], content = "null")
            newOne.save()


### test getProducts(productID) ###
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


