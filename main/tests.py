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

### test getProducts(productID) ###
    testProducts = ["aaaa","bbbb","cccc","dddd"]
    def setUp(self):
        for i in range(4):
            newOne = Product(category = "hats", name = testUnit.testProducts[i], brand = "null", \
                             url = "null", photo = "null", price = 1.0 )
            newOne.save()
        for i in range(4):
            newOne = Comment()

    def testGetProduct(self):
        baseModel = dataBaseModel()
        products = baseModel.getProducts("hats")
        for i in range(4):
            self.assertTrue(testUnit.testProducts[i] in products[0] and products[1] == testUnit.SUCCESS, "addProduct failed")

















    def setUp(self):
        newOne = User(user = 'abcd', password = 'abcd' )
        newOne.save()

    def testLogin(self):   ### good one
        dataUser = UsersModel()
        self.assertEqual(dataUser.login('abcd', 'abcd'), (UsersModel.SUCCESS, self.Good_Num ))  ### count = 2

    def testAdd(self):    ### good one
        dataUser = UsersModel()
        self.assertEqual(dataUser.add('123', '123'), (UsersModel.SUCCESS, self.Good_Num))

    def testLoginWrongPassWord(self): #### Error
        dataUser = UsersModel()
        self.assertEqual(dataUser.login('123', '456'), (UsersModel.ERR_BAD_CREDENTIALS, self.Err_Num))

    def testNullNull(self): #### Error
        dataUser = UsersModel()
        self.assertEqual(dataUser.login('', ''), (UsersModel.ERR_BAD_USERNAME, self.Err_Num))

    def testAddNullUserName(self):  ### Error
        dataUser = UsersModel()
        self.assertEqual(dataUser.add('', '456'), (UsersModel.ERR_BAD_USERNAME, self.Err_Num))

    def testAddNullPassWord(self):  ### good one
        dataUser = UsersModel()
        self.assertEqual(dataUser.add('abc', ''), (UsersModel.SUCCESS, self.Good_Num))

    def testAddLongUserName(self):  ## Error
        user = '1' * 130
        dataUser = UsersModel()
        self.assertEqual(dataUser.add(user, '1234'), (UsersModel.ERR_BAD_USERNAME, self.Err_Num))

    def testAddDuplicateUserName(self):### Error
        dataUser = UsersModel()
        self.assertEqual(dataUser.add('abcd', '456'), (UsersModel.ERR_USER_EXISTS, self.Err_Num))

    def testAddLongPassWord(self): ## Error
        password = '1' * 200
        dataUser = UsersModel()
        self.assertEqual(dataUser.add('kkkk', password), (UsersModel.ERR_BAD_PASSWORD, self.Err_Num))


    def testRestartFixture(self):
        dataUser = UsersModel()
        self.assertEqual(dataUser.TESTAPI_resetFixture(), UsersModel.SUCCESS)
        try:
            getUser = User.objects.get(user = '123')
            self.assertEqual(True, False)
        except:
            self.assertEqual(True, True)