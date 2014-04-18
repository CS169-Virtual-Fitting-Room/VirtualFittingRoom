from django.test import TestCase
from dataBaseModel import dataBaseModel
from main.models import Product
from main.models import Category
from main.models import Comment
from main.models import WishList
from main.models import Added
from main.models import TempProduct
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
        testDBModel.testCategory = []
        testDBModel.testComments = []
        testDBModel.testFitLists = []
        testDBModel.testOverlay = []
        testDBModel.testProducts = []
        testDBModel.testUsers = []
        testDBModel.testUsersID = []
        testDBModel.testWishLists = []
        
    def testGetTempProduct(self):
        db = dataBaseModel()
        self.assertTrue(db.getTempProduct(testDBModel.testUsersID[0], '1')[1] == dataBaseModel.SUCCESS, "Failed to get temp product user 0")
        self.assertTrue(db.getTempProduct(testDBModel.testUsersID[0], '1')[0].overlay == testDBModel.testOverlay[0], "Failed to get temp product user 0")
        
    def testGetTempProductWithBadUser(self):
        db = dataBaseModel()
        self.assertTrue(db.getTempProduct(100, '1')[1] == dataBaseModel.ERR_BAD_TOKEN, "Expect negative err code")
        self.assertTrue(db.getTempProduct(100, '1')[0] == None, "Expect negative err code")
        
    def testGetTempProductWithBadToken(self):
        db = dataBaseModel()
        self.assertTrue(db.getTempProduct(testDBModel.testUsersID[0], 'a')[1] == dataBaseModel.ERR_BAD_TOKEN, "Expect negative err code")
        self.assertTrue(db.getTempProduct(testDBModel.testUsersID[0], 'a')[0] == None, "Expect negative err code")
        
    def testRemoveTempProduct(self):
        db = dataBaseModel()
        self.assertTrue(db.removeTempProduct(testDBModel.testUsersID[0])[0] == testDBModel.testOverlay[0], "Remove temp product not returning correct image path")
        
    def testRemoveTempProductBadUserID(self):
        db = dataBaseModel()
        self.assertTrue(db.removeTempProduct(100) == [], "Remove temp product not returning empty image path")   
        
    def testAddTempProduct(self):
        db = dataBaseModel()
        db.addTempProduct(testDBModel.testUsersID[0],'testingtoken', 'testingoverlayol.jpg', 'glasses')
        queryset = TempProduct.objects.filter(Q(owner = testDBModel.testUsers[0]), Q(token='testingtoken'))
        self.assertTrue(queryset.count() == 1, 'Unable to add temp product')
       
    def testAddProduct(self):
        db = dataBaseModel()
        result = db.addProduct(testDBModel.testUsersID[3], "image.jpg", "overlayol.jpg", "glasses", "brand", "nameA", "www.url.com", 32, "testing description") 
        self.assertTrue(result == dataBaseModel.SUCCESS, "Add product not returning success")
        queryset = Product.objects.filter(name="nameA")
        self.assertTrue(queryset.count() == 1, "Add product not adding product to database")
        queryset = Added.objects.filter(owner = testDBModel.testUsers[3])
        self.assertTrue(queryset.count() == 1, "Add product not adding Added entry")
        
    def testAddProductBadCategory(self):   
        db = dataBaseModel()
        result = db.addProduct(testDBModel.testUsersID[3], "image.jpg", "overlayol.jpg", "wrong category", "brand", "nameA", "www.url.com", 32, "testing description") 
        self.assertTrue(result == dataBaseModel.ERR_UNABLE_TO_ADD_PRODUCT, "Add product not returning failure")
        queryset = Product.objects.filter(name="nameA")
        self.assertTrue(queryset.count() == 0, "Add product adding wrong product to database")
        queryset = Added.objects.filter(owner = testDBModel.testUsers[3])
        self.assertTrue(queryset.count() == 0, "Add product adding wrong Added entry")
        
    def testAddProductBadPrice(self):
        db = dataBaseModel()
        result = db.addProduct(testDBModel.testUsersID[3], "image.jpg", "overlayol.jpg", "wrong category", "brand", "nameA", "www.url.com", "badprice", "testing description") 
        self.assertTrue(result == dataBaseModel.ERR_UNABLE_TO_ADD_PRODUCT, "Add product not returning failure")
        queryset = Product.objects.filter(name="nameA")
        self.assertTrue(queryset.count() == 0, "Add product adding wrong product to database")
        queryset = Added.objects.filter(owner = testDBModel.testUsers[3])
        self.assertTrue(queryset.count() == 0, "Add product adding wrong Added entry")
        

    def testSearchProductNormal1(self):
        productList = ["ProductA", "ProductB", "ProductC", "ProductD"]
        db = dataBaseModel()
        result = db.searchProducts("pro")
        self.assertEquals(result[1], dataBaseModel.SUCCESS)
        for elem in result[0]:
            self.assertTrue(elem.name in productList)

    def testSearchProductNormal2(self):
        productList = ["ProductA", "ProductB", "ProductC", "ProductD"]
        db = dataBaseModel()
        result = db.searchProducts("ductA")
        self.assertEquals(result[1], dataBaseModel.SUCCESS)
        for elem in result[0]:
            self.assertEqual(elem.name, "ProductA")

    def testSearchProductNormal3(self):
        productList = ["ProductA", "ProductB", "ProductC", "ProductD"]
        db = dataBaseModel()
        result = db.searchProducts("")
        self.assertEquals(result[1], dataBaseModel.SUCCESS)
        for elem in result[0]:
            self.assertTrue(elem.name in productList)

    def testSearchProductWithBadName(self):
        db = dataBaseModel()
        result = db.searchProducts("AB")
        self.assertEquals(result[1], dataBaseModel.SUCCESS)
        self.assertEquals(len(result[0]), 0)

