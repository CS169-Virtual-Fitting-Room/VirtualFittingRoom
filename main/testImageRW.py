from django.test import TestCase
from main.ImageRW import ImageRW
import os
import httplib, mimetypes

class testImageRW(TestCase):
    
    def testReadImage(self):
        data = ImageRW.readImage('rayban.jpg')
        self.assertTrue(len(data) > 0, 'ImageRW not reading images')

    def testReadImageNonExistImage(self):
        data = ImageRW.readImage('notexist.jpg')
        self.assertTrue(len(data) == 0, 'ImageRW returning bytes of non existing image')
        
    def testProcessInPerm(self):
        ImageRW.Process("sample.jpg", True, "headphones")
        #ImageRW.convertToTransparent("apple.jpg", True)
        self.assertTrue(os.path.isfile(ImageRW.IMAGE_DIR + "sample.png"), 'Image not converted to PNG')
        
    def testProcessInTemp(self):
        
        ImageRW.Process("test1.jpg", False, "hats")
        ImageRW.Process("test2.jpg", False, "headphones")
        ImageRW.Process("test3.jpg", False, "headphones")
        ImageRW.Process("test4.jpg", False, "hats")
        ImageRW.Process("test5.jpg", False, "glasses")
        #self.assertTrue(os.path.isfile(ImageRW.TEMP_DIR + "sample.png"), 'Image not converted to PNG')
        
    
    def testRemoveImageInPermanent(self):
        ImageRW.removeImage("sample.png", True)
        self.assertTrue(os.path.isfile(ImageRW.IMAGE_DIR + "sample.png") == False, 'Image not removed')
        
    def testRemoveImageInTemp(self):
        ImageRW.removeImage("sample.png", False)
        self.assertTrue(os.path.isfile(ImageRW.TEMP_DIR + "sample.png") == False, 'Image not removed')
        

    def testRemoveNonExistImage(self):
        
        result = ImageRW.removeImage("wrongoneoops.jpg", True, True)
        self.assertEquals(result, True, "Incorrect remove image behavior")
     
    def testWriteImageInPerm(self):
        from django.core.files.uploadedfile import SimpleUploadedFile
        uploaded_file = open("testImage.jpg", 'rb')
        dfile = SimpleUploadedFile(uploaded_file.name, uploaded_file.read())
        self.assertEquals(ImageRW.writeImage(dfile, True, "testWrite.jpg"), "testWrite.jpg", "Unable to write image")
        
    def testWriteImageInTemp(self):
        from django.core.files.uploadedfile import SimpleUploadedFile
        uploaded_file = open("testImage.jpg", 'rb')
        dfile = SimpleUploadedFile(uploaded_file.name, uploaded_file.read())
        self.assertEquals(ImageRW.writeImage(dfile, False, "testWrite.jpg"), "testWrite.jpg", "Unable to write image")
        
    def testWriteVeryLargeImage(self):
        from django.core.files.uploadedfile import SimpleUploadedFile
        uploaded_file = open("verylarge.jpg", 'rb')
        dfile = SimpleUploadedFile(uploaded_file.name, uploaded_file.read())
        self.assertEquals(ImageRW.writeImage(dfile, True, "testWrite.jpg"), "", "Able to write large image")
        
    def testWriteWrongFormat(self):
        from django.core.files.uploadedfile import SimpleUploadedFile
        uploaded_file = open("wrongformat.png", 'rb')
        dfile = SimpleUploadedFile(uploaded_file.name, uploaded_file.read())
        self.assertEquals(ImageRW.writeImage(dfile, True, "testWrite.jpg"), "", "Able to write wrong format image")

    