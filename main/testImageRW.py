from django.test import TestCase
from main.ImageRW import ImageRW
import os

class testImageRW(TestCase):
    def testReadImage(self):
        data = ImageRW.readImage('rayban.jpg')
        self.assertTrue(len(data) > 0, 'ImageRW not reading images')

    def testReadImageNonExistImage(self):
        data = ImageRW.readImage('notexist.jpg')
        self.assertTrue(len(data) == 0, 'ImageRW returning bytes of non existing image')
        
    def testConvertToTransparentInPermanent(self):
        ImageRW.convertToTransparent("sample.jpg", True)
        self.assertTrue(os.path.isfile(ImageRW.IMAGE_DIR + "sample.png"), 'Image not converted to PNG')
        
    def testConvertToTransparentInTemp(self):
        ImageRW.convertToTransparent("sample.jpg", False)
        self.assertTrue(os.path.isfile(ImageRW.TEMP_DIR + "sample.png"), 'Image not converted to PNG')
        
    def testRemoveImageInPermanent(self):
        ImageRW.removeImage("sample.png", True)
        self.assertTrue(os.path.isfile(ImageRW.IMAGE_DIR + "sample.png") == False, 'Image not removed')
        
    def testRemoveImageInTemp(self):
        ImageRW.removeImage("sample.png", False)
        self.assertTrue(os.path.isfile(ImageRW.TEMP_DIR + "sample.png") == False, 'Image not removed')