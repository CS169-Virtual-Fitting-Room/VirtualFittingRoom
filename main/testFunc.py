from django.test import TestCase
import httplib
import json

class testFunc (TestCase):
    SERVER = 'localhost:8000'
    def setUp(self):
        self.conn = httplib.HTTPConnection(testFunc.SERVER, timeout = 1)
        
    def tearDown(self):
        self.conn.close()
        
    # load the index page
    def testIndex(self):
        self.conn.request('GET', '/')
        resp = self.conn.getresponse()
        self.assertTrue(resp.status == 200, 'Can\'t make request to server')
        data = resp.read()
        self.assertTrue('<title>Virtual Fitting Room</title>' in data, 'Index page not loaded')
        
    # load the category page
    def testCategory(self):
        self.conn.request('GET', '/glasses/')
        resp = self.conn.getresponse()
        self.assertTrue(resp.status == 200, 'Can\'t make request to server')
        data = resp.read()
        self.assertTrue('rendergrids' in data, 'Category list page not loaded')
        
        self.conn.request('GET', '/hats/')
        resp = self.conn.getresponse()
        self.assertTrue(resp.status == 200, 'Can\'t make request to server')
        data = resp.read()
        self.assertTrue('rendergrids' in data, 'Category list page not loaded')
        
        self.conn.request('GET', '/headphones/')
        resp = self.conn.getresponse()
        self.assertTrue(resp.status == 200, 'Can\'t make request to server')
        data = resp.read()
        self.assertTrue('rendergrids' in data, 'Category list page not loaded')
        
        self.conn.request('GET', '/somerandomcategory12342/')
        resp = self.conn.getresponse()
        self.assertTrue(resp.status == 200, 'Can\'t make request to server')
        data = resp.read()
        self.assertTrue('rendergrids' in data, 'Category list page not loaded')
        
    # test ajax call to /<category>/<list>
    def testCategoryList(self):
        self.assertValidCategoryListRequest('/glasses/list/')
        self.assertValidCategoryListRequest('/hats/list/')
        self.assertValidCategoryListRequest('/headphones/list/')
        
        self.assertInvalidCategoryListRequest('/randomcategory/list/')
     
    # test load detail page   
    def testDetailPage(self):
        self.conn.request('GET', '/glasses/rayban%20glasses/')
        resp = self.conn.getresponse()
        self.assertTrue(resp.status == 200, 'Can\'t make request to server')
        data = resp.read()
        self.assertTrue('<title>Detail Page</title>' in data, 'Detail page not loaded')
        
        self.conn.request('GET', '/hats/adidas%20cap/')
        resp = self.conn.getresponse()
        self.assertTrue(resp.status == 200, 'Can\'t make request to server')
        data = resp.read()
        self.assertTrue('<title>Detail Page</title>' in data, 'Detail page not loaded')
        
        self.conn.request('GET', '/headphones/beats%20headphones/')
        resp = self.conn.getresponse()
        self.assertTrue(resp.status == 200, 'Can\'t make request to server')
        data = resp.read()
        self.assertTrue('<title>Detail Page</title>' in data, 'Detail page not loaded')
        
        self.conn.request('GET', '/somerandomcategory/somerandomproduct/')
        resp = self.conn.getresponse()
        self.assertTrue(resp.status == 200, 'Can\'t make request to server')
        data = resp.read()
        self.assertTrue('<title>Detail Page</title>' in data, 'Detail page not loaded')
        
    # test load product detail
    def testProductDetail(self):
        self.assertValidProductDetailRequest('/glasses/rayban%20glasses/info/')
        self.assertValidProductDetailRequest('/hats/adidas%20cap/info/')
        self.assertInvalidProductDetailRequest('/somecategory/someproduct/info/')
        
    def assertValidCategoryListRequest(self, url):
        self.conn.request('GET', url)
        resp = self.conn.getresponse()
        self.assertTrue(resp.status == 200, 'Can\'t make request to server')
        self.assertTrue(resp.getheader('content-type') is not None, "content-type header must be present in the response")
        self.assertTrue(resp.getheader('content-type').find('application/json') == 0, "content-type header must be application/json")
        rawdata = resp.read()
        jsondata = json.loads(rawdata)
        self.assertTrue('item_name' in jsondata and 'category_name' in jsondata and 'image' in jsondata and 'price' in jsondata, 'json respond is not correct')
        self.assertTrue(len(jsondata['item_name']) > 0, 'Respond json has no items.')
        self.assertTrue(len(jsondata['category_name']) != 0, 'Respond json has no category name')
        self.assertTrue(len(jsondata['image']) != 0, 'Respond json has no image')
        self.assertTrue(len(jsondata['price']) != 0, 'Respond json has no price')
        
    def assertInvalidCategoryListRequest(self, url):
        self.conn.request('GET', url)
        resp = self.conn.getresponse()
        self.assertTrue(resp.status == 200, 'Can\'t make request to server')
        self.assertTrue(resp.getheader('content-type') is not None, "content-type header must be present in the response")
        self.assertTrue(resp.getheader('content-type').find('application/json') == 0, "content-type header must be application/json")
        rawdata = resp.read()
        jsondata = json.loads(rawdata)
        self.assertTrue('item_name' in jsondata and 'category_name' in jsondata and 'image' in jsondata and 'price' in jsondata, 'json respond is not correct')
        self.assertTrue(len(jsondata['item_name']) == 0, 'Respond json has items.')
        self.assertTrue(len(jsondata['category_name']) == 0, 'Respond json has category name')
        self.assertTrue(len(jsondata['image']) == 0, 'Respond json has image')
        self.assertTrue(len(jsondata['price']) == 0, 'Respond json has price')
        
    def assertValidProductDetailRequest(self, url):
        self.conn.request('GET', url)
        resp = self.conn.getresponse()
        self.assertTrue(resp.status == 200, 'Can\'t make request to server')
        self.assertTrue(resp.getheader('content-type') is not None, "content-type header must be present in the response")
        self.assertTrue(resp.getheader('content-type').find('application/json') == 0, "content-type header must be application/json")
        rawdata = resp.read()
        jsondata = json.loads(rawdata)
        self.assertTrue('item_name' in jsondata and 'description' in jsondata and 'image' in jsondata and 'price' in jsondata, 'json respond is not correct')
        self.assertTrue(jsondata['item_name'] != '', 'Respond json has no items.')
        self.assertTrue(jsondata['image'] != '', 'Respond json has no image')
        self.assertTrue(jsondata['price'] != -1, 'Respond json has no price')
        
    def assertInvalidProductDetailRequest(self, url):
        self.conn.request('GET', url)
        resp = self.conn.getresponse()
        self.assertTrue(resp.status == 200, 'Can\'t make request to server')
        self.assertTrue(resp.getheader('content-type') is not None, "content-type header must be present in the response")
        self.assertTrue(resp.getheader('content-type').find('application/json') == 0, "content-type header must be application/json")
        rawdata = resp.read()
        jsondata = json.loads(rawdata)
        self.assertTrue('item_name' in jsondata and 'description' in jsondata and 'image' in jsondata and 'price' in jsondata, 'json respond is not correct')
        self.assertTrue(jsondata['item_name'] == '', 'Respond json has no items.')
        self.assertTrue(jsondata['description'] == '', 'Respond json has description')
        self.assertTrue(jsondata['image'] == '', 'Respond json has no image')
        self.assertTrue(jsondata['price'] == -1, 'Respond json has no price')
        
        
        