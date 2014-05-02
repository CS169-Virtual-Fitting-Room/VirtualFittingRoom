from django.test import TestCase
from dataBaseModel import dataBaseModel
from main.models import Product
from main.models import Category
from main.models import Comment
from main.models import WishList
from main.models import Added
from main.models import TempProduct
from main.models import User
from django.contrib.auth.models import User as AUser
from django.utils import timezone
from main.models import FitList
from django.db.models import Q

# ##    Create your tests here.

class testDBModel(TestCase):
    """
    SUCCESS = 1
    ERR_BAD_PRODUCT = -1
    ERR_BAD_USER = -2
    ERR_UNABLE_TO_REMOVE_FROM_WISHLIST = -3
    ERR_BAD_CATEGORY = -4
    ERR_UNABLE_TO_REMOVE_FROM_FITLIST = -5
    """

    testUsers = []
    testUsersID = []
    testCategory = []
    testProducts = []
    testComments = []
    testWishLists = []
    testFitLists = []
    testOverlay = []


    def setUp(self):
###### create Users #######
        users = ['UserA', 'UserB', 'UserC', 'UserD']
        for i in range(4):
            newUser = AUser(password='', last_login=timezone.now(), is_superuser=True, username=users[i], first_name='Firstname', last_name='Lastname', email='a@email.com', is_staff=True, is_active=True, date_joined=timezone.now())
            newUser.save()
            testDBModel.testUsers.append(newUser)
            testDBModel.testUsersID.append(newUser.pk)

######  add Category ######
        category1 = Category(name="hats")
        testDBModel.testCategory.append(category1)
        category1.save()
        category2 = Category(name="glasses")
        testDBModel.testCategory.append(category2)
        category2.save()
        
        user = User(id=testDBModel.testUsersID[0],user_id=testDBModel.testUsersID[0], user_image="profile1.jpg")
        user.save()

######   add product ######
        addProducts = ["ProductA", "ProductB", "ProductC", "ProductD"]
        for i in range(4):  # # add products
            newOne = Product(category=category1, name=addProducts[i], brand='brand', url='url', photo='photo', price=1.0, description='')
            newOne.save()
            testDBModel.testProducts.append(newOne)

######  add custom product #####
        newAdded = Added(owner = testDBModel.testUsers[0], product = testDBModel.testProducts[0])
        newAdded.save()
        newAdded = Added(owner = testDBModel.testUsers[1], product = testDBModel.testProducts[1])
        newAdded.save()
        
######  add temp product ######
        tempP = TempProduct(owner = testDBModel.testUsers[0], overlay = 'overlay1ol.jpg', token = '1', category = testDBModel.testCategory[0])
        tempP.save()
        tempP = TempProduct(owner = testDBModel.testUsers[1], overlay = 'overlay2ol.jpg', token = '2', category = testDBModel.testCategory[0])
        tempP.save()
        testDBModel.testOverlay = ['overlay1ol.jpg', 'overlay2ol.jpg']

##### ## add comments   ######
        for i in range(4):
            newOne = Comment(product=testDBModel.testProducts[i], owner=testDBModel.testUsers[i], content="null", time = timezone.now())
            newOne.save()
            testDBModel.testComments.append(newOne)

# add to wishlist first
        for i in range(4):
            newOne = WishList(product=testDBModel.testProducts[i], owner=testDBModel.testUsers[i])
            newOne.save()

# add to FitList:
        for i in range(4):
            newOne = FitList(product = testDBModel.testProducts[i], owner = testDBModel.testUsers[i])
            newOne.save()

    def tearDown(self):
        WishList.objects.all().delete()
        Comment.objects.all().delete()
        Product.objects.all().delete()
        Category.objects.all().delete()
        FitList.objects.all().delete()
        Added.objects.all().delete()
        TempProduct.objects.all().delete()
        User.objects.all().delete()
        
        testDBModel.testCategory = []
        testDBModel.testComments = []
        testDBModel.testFitLists = []
        testDBModel.testOverlay = []
        testDBModel.testProducts = []
        testDBModel.testUsers = []
        testDBModel.testUsersID = []
        testDBModel.testWishLists = []
        
    def testCheckIfOwnCustomProduct(self):
        db = dataBaseModel()
        result = db.checkIfOwnCustomProduct(testDBModel.testUsersID[0], testDBModel.testProducts[0].id)
        self.assertTrue(result, "Failed to verify user own products")

    def testCheckIfOwnCustomProductBadProduct(self):
        db = dataBaseModel()
        result = db.checkIfOwnCustomProduct(testDBModel.testUsersID[0], testDBModel.testProducts[1].id)
        self.assertFalse(result, "Failed to verify user own products")

    def testRemoveCustomProduct(self):
        db = dataBaseModel()
        result = db.removeCustomProduct(testDBModel.testUsersID[0], testDBModel.testProducts[0].id)
        self.assertTrue(result == dataBaseModel.SUCCESS, "Unable to remove custom product")
        
    def testRemoveCustomProductBadProduct(self):
        db = dataBaseModel()
        result = db.removeCustomProduct(testDBModel.testUsersID[0], testDBModel.testProducts[1].id)
        self.assertTrue(result == dataBaseModel.ERR_UNABLE_TO_REMOVE_CUSTOM_PRODUCT, "Able to remove custom product that doesn't belong to user")        
        
    def testGetCustomProduct(self):
        db = dataBaseModel()
        result = db.getCustomProduct(testDBModel.testUsersID[0])
        self.assertTrue(result[0].id == 1, "Unable to get custom product")
   
    def testGetCustomProductBadID(self):
        db = dataBaseModel()
        result = db.getCustomProduct(100)
        self.assertTrue(result == [], "Empty list not retrieved")
        
    def testAddProfilePic(self):
        db = dataBaseModel()
        db.addProfilePic(testDBModel.testUsersID[1], "test.jpg")
        queryset = User.objects.filter(user_image = "test.jpg")
        self.assertTrue(queryset.count() == 1, "Unable to add profile pic")
        
    def testReplaceProfilePic(self):
        db = dataBaseModel()
        db.addProfilePic(testDBModel.testUsersID[0], "newprofile.jpg")
        queryset1 = User.objects.filter(user_image="profile1.jpg")
        queryset2 = User.objects.filter(user_image="newprofile.jpg")
        self.assertTrue(queryset1.count() == 0 and queryset2.count() == 1, 'Unable to replace existing profile picture')   
        
    def testGetProfilePic(self):
        db = dataBaseModel()
        result = db.getProfilePic(testDBModel.testUsersID[0])   
        self.assertTrue(result == "profile1.jpg", "Unable to get profile pic")
        
    def testGetProfilePicBadUserID(self):
        db = dataBaseModel()
        result = db.getProfilePic(100)   
        self.assertTrue(result == "", "Unable to retrieve empty string for invalid user id")
        
    def testGetNumAdded(self):
        db = dataBaseModel()
        result = db.getNumAdded(testDBModel.testUsersID[0])
        self.assertTrue(result == 1, "Unable to get correct num added custom item")    
    
    def testGetNumAddedBadUseID(self):
        db = dataBaseModel()
        result = db.getNumAdded(100)
        self.assertTrue(result == 0, "Wrong num of custom item added when invalid user id")    
        
    def testGetUserInfo(self):
        db = dataBaseModel()
        result = db.getUserInfo(testDBModel.testUsersID[0])
        self.assertTrue(result == testDBModel.testUsers[0], "Unable to get correct user info")
        
    def testGetUserInfoBadUserID(self):
        db = dataBaseModel()
        result = db.getUserInfo(100)
        self.assertTrue(result == "", "Unable to retrieve empty string on invalid user id")
        
    def testEditProduct(self):
        db = dataBaseModel()
        result = db.editProduct(testDBModel.testUsersID[0], "changed.jpg", "changedol.jpg","glasses", "brand", "newproduct1", "randomurl", 24, "changed description", testDBModel.testProducts[0].id)
        self.assertTrue(result == dataBaseModel.SUCCESS, "Unable to edit custom item")
        queryset = Product.objects.filter(name="newproduct1")
        self.assertTrue(queryset.count() == 1, "Edited name not updated")
        
    def testEditProductBadUserID(self):
        db = dataBaseModel()
        result = db.editProduct(100, "changed.jpg", "changedol.jpg","glasses", "brand", "newproduct1", "randomurl", 24, "changed description", testDBModel.testProducts[0].id)
        self.assertTrue(result == dataBaseModel.ERR_UNABLE_TO_EDIT_CUSTOM_PRODUCT, "Unable to edit custom item")
        
    def testEditProductOtherProductID(self):
        db = dataBaseModel()
        result = db.editProduct(testDBModel.testUsersID[0], "changed.jpg", "changedol.jpg","glasses", "brand", "newproduct1", "randomurl", 24, "changed description", testDBModel.testProducts[1].id)
        self.assertTrue(result == dataBaseModel.ERR_UNABLE_TO_EDIT_CUSTOM_PRODUCT, "Able to edit other custom item") 
        
    def testEditProductBadProductID(self):
        db = dataBaseModel()
        result = db.editProduct(testDBModel.testUsersID[0], "changed.jpg", "changedol.jpg","glasses", "brand", "newproduct1", "randomurl", 24, "changed description", 100)
        self.assertTrue(result == dataBaseModel.ERR_UNABLE_TO_EDIT_CUSTOM_PRODUCT, "Did not prompt error on bad product id") 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        