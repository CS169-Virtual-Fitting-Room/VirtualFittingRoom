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
        self.assertTrue(os.path.isfile(ImageRW.IMAGE_DIR + "sampleol.png"), 'Image not converted to PNG')