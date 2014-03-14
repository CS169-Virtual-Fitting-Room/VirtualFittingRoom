from django.test import TestCase
from dataBaseModel import dataBaseModel
from main.models import Product
from main.models import Category
from main.models import Comment
from main.models import WishList
from django.contrib.auth.models import User as AUser
from django.utils import timezone
###    Create your tests here.

###    google account: fittingroomtem@gmail.com
###    password : berkeleycs169

class testUnit(TestCase):
    SUCCESS = 1
    ERR_BAD_PRODUCT = -1
    ERR_BAD_USER = -2
    ERR_UNABLE_TO_REMOVE_FROM_WISHLIST = -3
    ERR_BAD_CATEGORY = -4

    testUsers = []
    testUsersID = []
    testCategory = []
    testProducts = []
    testComments = []
    testWishLists = []
    
    
    def setUp(self):
###### create Users #######
        import datetime
        users = ['UserA', 'UserB', 'UserC', 'UserD']
        for i in range(4):
            newUser = AUser(password = '', last_login = timezone.now(), is_superuser = True, username = users[i], first_name = 'Firstname', last_name = 'Lastname', email = 'a@email.com', is_staff = True, is_active = True, date_joined = timezone.now())
            newUser.save()
            testUnit.testUsers.append(newUser)
            testUnit.testUsersID.append(newUser.pk)
######  add Category ######
        category1 = Category(name = "hats")
        testUnit.testCategory.append(category1)
        category1.save()


######   add product ######
        addProducts = ["ProductA","ProductB","ProductC","ProductD"]
        for i in range(4):  ## add products
            newOne = Product(category = category1, name = addProducts[i], brand = 'brand', url = 'url', photo = 'photo', price = 1.0, description = '')
            newOne.save()
            testUnit.testProducts.append(newOne)

##### ## add comments   ######
        for i in range(4):
            newOne = Comment(product = testUnit.testProducts[i], owner = testUnit.testUsers[i], content = "null")
            newOne.save()
            testUnit.testComments.append(newOne)

# add to wishlist first
        for i in range(4):
            newOne = WishList(product = testUnit.testProducts[i], owner = testUnit.testUsers[i])
            newOne.save()
            
    def tearDown(self):
        WishList.objects.all().delete()
        Comment.objects.all().delete()
        Product.objects.all().delete()
        Category.objects.all().delete()



    def testGetProducts(self):
        baseModel = dataBaseModel()
        products = baseModel.getProducts(testUnit.testCategory[0])
  
        self.assertTrue(set(testUnit.testProducts) == set(products[0]) and products[1] == testUnit.SUCCESS, "getProduct failed")


    def testGetDetailWithValidProductName(self):
        baseModel = dataBaseModel()
        for i in range(4):
            productDetail = baseModel.getDetail(testUnit.testProducts[i])
            self.assertTrue(productDetail != None, "getDetail failed, can not find the product")
            self.assertTrue(productDetail[0].category == testUnit.testCategory[0], "getDetail failed, wrong category")
            self.assertTrue(productDetail[0].brand == "brand", "getDetail failed, wrong brand")
            self.assertTrue(productDetail[0].url == "url", "getDetail failed, wrong url")
            self.assertTrue(productDetail[0].photo == "photo", "getDetail failed, wrong photo")
            self.assertTrue(productDetail[0].price == 1.0, "getDetail failed, wrong price")
            
    def testGetDetailWithNonExistingProductName(self):
        baseModel = dataBaseModel()
        productDetail = baseModel.getDetail("non-existing")
        self.assertTrue(productDetail[0] == None, "getDetail failed, can not detect non exist product")


    def testAddToWishList(self):
        baseModel = dataBaseModel()
        WishList.objects.all().delete()
        from django.db.models import Q
        for i in range(4):
            response = baseModel.addToWishList(testUnit.testUsersID[i], testUnit.testProducts[i].name)
            queryset = WishList.objects.filter(Q(owner = testUnit.testUsers[i]), Q(product = testUnit.testProducts[i]))
            self.assertTrue(response == testUnit.SUCCESS and queryset.count() == 1, "addToWishList failed, can not add")


    def testRemoveFromWishList(self):
        baseModel = dataBaseModel()
        from django.db.models import Q
                   
        for i in range(4):
            response = baseModel.removeFromWishList(testUnit.testUsersID[i], testUnit.testProducts[i].name)
            queryset = WishList.objects.filter(Q(owner = testUnit.testUsers[i]), Q(product = testUnit.testProducts[i]))
            self.assertTrue(response == testUnit.SUCCESS and queryset.count() == 0, "can not do removeFromWishList")

    def testRemoveFromWishListWithBadProduct(self):
        baseModel = dataBaseModel()
        response = baseModel.removeFromWishList(testUnit.testUsersID[0], "Wrong Product")
        self.assertTrue(response == testUnit.ERR_UNABLE_TO_REMOVE_FROM_WISHLIST, "remove non-exist wishlist")

    def testRemoveFromWishListWithBadUser(self):
        baseModel = dataBaseModel()
        response = baseModel.removeFromWishList(100, testUnit.testProducts[0])
        self.assertTrue(response == testUnit.ERR_UNABLE_TO_REMOVE_FROM_WISHLIST, "remove non-exist wishlist")


    def testGetWishList(self):
        baseModel = dataBaseModel()
        for i in range(4):
            response = baseModel.getWishList(testUnit.testUsersID[i])
            self.assertTrue(response[1] == testUnit.SUCCESS and len(response[0]) > 0, "can not get WishList")

    def testGetWishListFromNonExistUser(self):
        baseModel = dataBaseModel()
        response = baseModel.getWishList(6)  ## "e" user does not exist
        self.assertTrue(response[1] == testUnit.ERR_BAD_USER and len(response[0]) == 0, "get wishList from non exist user")



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

