from django.test import TestCase
from dataBaseModel import dataBaseModel
from main.models import Product
from main.models import Category
from main.models import Comment
from main.models import WishList
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


######   add product ######
        addProducts = ["ProductA", "ProductB", "ProductC", "ProductD"]
        for i in range(4):  # # add products
            newOne = Product(category=category1, name=addProducts[i], brand='brand', url='url', photo='photo', price=1.0, description='')
            newOne.save()
            testDBModel.testProducts.append(newOne)

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

####  get Fit List
    def testGetFitList(self):
        baseModel = dataBaseModel()
        for i in range(4):
            response = baseModel.getFitList(testDBModel.testUsersID[i])
            self.assertTrue(response[1] == dataBaseModel.SUCCESS and len(response[0]) > 0, "can's get the Fit List")

    def testGetFitListFromNonExistUser(self):
        baseModel = dataBaseModel()
        response = baseModel.getFitList(6)
        self.assertTrue(response[1] == dataBaseModel.ERR_BAD_USER and len(response[0]) == 0, "get fit list from a non exist user")


###  add to fit list
    def testAddToFitList(self):
        baseModel = dataBaseModel()
        FitList.objects.all().delete()
        for i in range(4):
            response = baseModel.addToFitList(testDBModel.testUsersID[i], testDBModel.testProducts[i], i+1 )
            queryset = FitList.objects.filter(Q(owner = testDBModel.testUsers[i]), Q(product = testDBModel.testProducts[i]))
            self.assertTrue(response == dataBaseModel.SUCCESS and queryset.count() == 1, "addTo FitList failed")

    def testAddToFitListWithBadProductID(self):
        baseModel = dataBaseModel()
        FitList.objects.all().delete()
        response = baseModel.addToFitList(testDBModel.testUsersID[0], testDBModel.testProducts[0], 10)
        self.assertTrue(response == dataBaseModel.ERR_BAD_PRODUCT, "add non exist product to fit list")


    def testAddtoFitListWithBadProductName(self):
        baseModel = dataBaseModel()
        FitList.objects.all().delete()
        response = baseModel.addToFitList(testDBModel.testUsersID[0], 'bad product', 1)
        self.assertTrue(response == dataBaseModel.ERR_BAD_PRODUCT, " add non exist product to fit list")



### remove from fit list

    def testRemoveFromFitList(self):
        baseModel = dataBaseModel()
        for i in range(4):
            response = baseModel.removeFromFitList(testDBModel.testUsersID[i], testDBModel.testProducts[i], i+1)
            queryset = FitList.objects.filter(Q(owner = testDBModel.testUsersID[i]), Q(product = testDBModel.testProducts[i]))
            self.assertTrue(response == dataBaseModel.SUCCESS and queryset.count() == 0, " can not do removeFromFitList")

    def testRemoveFromFitListWithBadProductID(self):
        baseModel = dataBaseModel()
        response = baseModel.removeFromFitList(testDBModel.testUsersID[0], testDBModel.testProducts[0], 20)
        self.assertTrue(response == dataBaseModel.ERR_UNABLE_TO_REMOVE_FROM_FITLIST, "remove non exist product from fit list")

    def testRemoveFromFitListwithBadProduct(self):
        baseModel = dataBaseModel()
        response = baseModel.removeFromFitList(testDBModel.testUsersID[0], 'bad product', 1 )
        self.assertTrue(response == dataBaseModel.ERR_UNABLE_TO_REMOVE_FROM_FITLIST, "remove non exist product from fit list")

