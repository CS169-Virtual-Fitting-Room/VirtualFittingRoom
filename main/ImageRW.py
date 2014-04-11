import os
from PIL import Image

class ImageRW:
    
    IMAGE_DIR = os.path.dirname(os.path.realpath(__file__)) + "/static/products/"
    
    def __init__(self):
        pass
    
    @staticmethod
    def readImage(path): # reads the binary data of an image
        try:
            f = open(ImageRW.IMAGE_DIR + path, "rb")
            byte = f.read()
        except:
            return ''
        return byte
    
    @staticmethod
    def writeImage(file):
        #return the image path
        pass
    
    @staticmethod
    def removeImage(file):
        pass
    
    @staticmethod
    def convertToTransparent(image):
        pass
        