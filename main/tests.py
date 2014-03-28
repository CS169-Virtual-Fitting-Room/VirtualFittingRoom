from django.test import TestCase
from dataBaseModel import dataBaseModel
from main.models import Product
from main.models import Category
from main.models import Comment
from main.models import WishList
from main.ImageRW import ImageRW
from django.contrib.auth.models import User as AUser
from django.utils import timezone
# ##    Create your tests here.

class testDBModel(TestCase):

    testUsers = []
    testUsersID = []
    testCategory = []
    testProducts = []
    testComments = []
    testWishLists = []
    
    
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
            
    def tearDown(self):
        WishList.objects.all().delete()
        Comment.objects.all().delete()
        Product.objects.all().delete()
        Category.objects.all().delete()



    def testGetProducts(self):
        baseModel = dataBaseModel()
        products = baseModel.getProducts(testDBModel.testCategory[0].name)
        self.assertTrue(set(testDBModel.testProducts) == set(products[0]) and products[1] == dataBaseModel.SUCCESS, "getProduct failed")

    def testGetProductsWithBadCategory(self):
        baseModel = dataBaseModel()
        products = baseModel.getProducts('non exist category')
        self.assertTrue(products[0] == [] and products[1] == dataBaseModel.ERR_BAD_CATEGORY, 'getProducts returning products for non exist category')

    def testGetDetailWithValidProductID(self):
        baseModel = dataBaseModel()
        for i in range(4):
            productDetail = baseModel.getDetail(testDBModel.testProducts[i], i+1) # pk starts from 1
            self.assertTrue(productDetail != None, "getDetail failed, can not find the product")
            self.assertTrue(productDetail[0].category == testDBModel.testCategory[0], "getDetail failed, wrong category")
            self.assertTrue(productDetail[0].brand == "brand", "getDetail failed, wrong brand")
            self.assertTrue(productDetail[0].url == "url", "getDetail failed, wrong url")
            self.assertTrue(productDetail[0].photo == "photo", "getDetail failed, wrong photo")
            self.assertTrue(productDetail[0].price == 1.0, "getDetail failed, wrong price")
               
    def testGetDetailWithNonExistingProductName(self):
        baseModel = dataBaseModel()
        productDetail = baseModel.getDetail("non-existing", 1)
        self.assertTrue(productDetail[0] == None, "getDetail failed, can not detect non exist product")
        
        
    def testGetDetailWithBadID(self):
        baseModel = dataBaseModel()
        productDetail = baseModel.getDetail(testDBModel.testProducts[0],10)
        self.assertTrue(productDetail[0] == None, "getDetail failed, can not detect bad ID")


    def testAddToWishList(self):
        baseModel = dataBaseModel()
        WishList.objects.all().delete()
        from django.db.models import Q
        for i in range(4):
            response = baseModel.addToWishList(testDBModel.testUsersID[i], testDBModel.testProducts[i], i+1)
            queryset = WishList.objects.filter(Q(owner=testDBModel.testUsers[i]), Q(product=testDBModel.testProducts[i]))
            self.assertTrue(response == dataBaseModel.SUCCESS and queryset.count() == 1, "addToWishList failed, can not add")

    def testAddToWishListWithBadProductID(self):
        baseModel = dataBaseModel()
        WishList.objects.all().delete()
        response = baseModel.addToWishList(testDBModel.testUsersID[0], testDBModel.testProducts[0], 20)
        self.assertTrue(response == dataBaseModel.ERR_BAD_PRODUCT, 'addToWishList adding non existing product')
        
    def testAddToWishListWithBadProductName(self):
        baseModel = dataBaseModel()
        WishList.objects.all().delete()
        response = baseModel.addToWishList(testDBModel.testUsersID[0], 'bad product', 1)
        self.assertTrue(response == dataBaseModel.ERR_BAD_PRODUCT, 'addToWishList adding non existing product')
        
    """
    def testAddToWishListWithBadUser(self):
        baseModel = dataBaseModel()
        WishList.objects.all().delete()
        response = baseModel.addToWishList(6, 1)
        self.assertTrue(response == testDBModel.ERR_BAD_USER, 'addToWishList adding product to non existing user')
    """
    
    def testRemoveFromWishList(self):
        baseModel = dataBaseModel()
        from django.db.models import Q
                   
        for i in range(4):
            response = baseModel.removeFromWishList(testDBModel.testUsersID[i], testDBModel.testProducts[i], i+1)
            queryset = WishList.objects.filter(Q(owner=testDBModel.testUsers[i]), Q(product=testDBModel.testProducts[i]))
            self.assertTrue(response == dataBaseModel.SUCCESS and queryset.count() == 0, "can not do removeFromWishList")

    def testRemoveFromWishListWithBadProduct(self):
        baseModel = dataBaseModel()
        response = baseModel.removeFromWishList(testDBModel.testUsersID[0], testDBModel.testProducts[0], 20)
        self.assertTrue(response == dataBaseModel.ERR_UNABLE_TO_REMOVE_FROM_WISHLIST, "remove non-exist wishlist")

    def testRemoveFromWishListWithBadProductID(self):
        baseModel = dataBaseModel()
        response = baseModel.removeFromWishList(100, 'bad product', 1)
        self.assertTrue(response == dataBaseModel.ERR_UNABLE_TO_REMOVE_FROM_WISHLIST, "remove non-exist wishlist")


    def testGetWishList(self):
        baseModel = dataBaseModel()
        for i in range(4):
            response = baseModel.getWishList(testDBModel.testUsersID[i])
            self.assertTrue(response[1] == dataBaseModel.SUCCESS and len(response[0]) > 0, "can not get WishList")

    def testGetWishListFromNonExistUser(self):
        baseModel = dataBaseModel()
        response = baseModel.getWishList(6)  # # "e" user does not exist
        self.assertTrue(response[1] == dataBaseModel.ERR_BAD_USER and len(response[0]) == 0, "get wishList from non exist user")



    def testAddComment(self):
        baseModel = dataBaseModel()
        for i in range(4):
            response = baseModel.addComment(testDBModel.testUsersID[i],testDBModel.testProducts[i], i+1, "this is comment from user " + str(i), time = timezone.now())
            self.assertTrue(response == dataBaseModel.SUCCESS, "add comment not success")

    def testAddCommentWithBadProductID(self):
        baseModel = dataBaseModel()
        response = baseModel.addComment(testDBModel.testUsersID[0],testDBModel.testProducts[0], 20, "this is comment is on a non existing product", time=timezone.now())
        self.assertTrue(response == dataBaseModel.ERR_BAD_PRODUCT, " added comment to non exist product")

    def testAddCommentWithBadProductName(self):
        baseModel = dataBaseModel()
        response = baseModel.addComment(testDBModel.testUsersID[0],'bad product', 1, "this is comment is on a non existing product", time=timezone.now())
        self.assertTrue(response == dataBaseModel.ERR_BAD_PRODUCT, " added comment to non exist product")
    """
    def testAddCommentWithBadUser(self):
        baseModel = dataBaseModel()
        response = baseModel.addComment(6, 1, "this is comment from a non-existing user", time=timezone.now())
        self.assertTrue(response == testDBModel.ERR_BAD_USER, "added comment to non-exist user")
    """


    def testGetComments(self):
        baseModel = dataBaseModel()
        for i in range(4):
            temp = testDBModel.testComments[i]
            response = baseModel.getComments(testDBModel.testProducts[i],i+1)
            self.assertTrue(temp in response[0] and response[1] == dataBaseModel.SUCCESS, " can not find the comment")

    def testGetCommentsWithBadProductID(self):
        baseModel = dataBaseModel()
        response = baseModel.getComments(testDBModel.testProducts[0],20)  # product not exist
        self.assertTrue(response[0] == [] and response[1] == dataBaseModel.ERR_BAD_PRODUCT, "got comment from a non exist product")

    def testGetCommentsWithBadProductName(self):
            baseModel = dataBaseModel()
            response = baseModel.getComments('bad product',1)  # product not exist
            self.assertTrue(response[0] == [] and response[1] == dataBaseModel.ERR_BAD_PRODUCT, "got comment from a non exist product")

class testImageRW(TestCase):
    def testReadImage(self):
        data = ImageRW.readImage('rayban.jpg')
        self.assertTrue(len(data) > 0, 'ImageRW not reading images')

    def testReadImageNonExistImage(self):
        data = ImageRW.readImage('notexist.jpg')
        self.assertTrue(len(data) == 0, 'ImageRW returning bytes of non existing image')
        
        