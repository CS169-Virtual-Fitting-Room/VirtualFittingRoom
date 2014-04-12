import os
from PIL import Image
from django.core.files.base import File

class ImageRW:
    
    IMAGE_DIR = os.path.dirname(os.path.realpath(__file__)) + "/static/products/"
    TEMP_DIR = os.path.dirname(os.path.realpath(__file__)) + "/static/temp/"
    SUCCESS = 1
    ERR_WRONG_FORMAT = -1
    ERR_IMAGE_TOO_LARGE = -2
    
    
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
    def writeImage(file, permanent): # file is of type UploadedFile
        #return the image path
        if file.size > 3000000: # larger than 3 MB
            return ImageRW.ERR_IMAGE_TOO_LARGE
        if not (file.name[-4:] == '.jpg' or file.name[-5:] == '.jpeg'): # check format
            return ImageRW.ERR_WRONG_FORMAT
        
        filename = file.name
        path = ""
        if permanent :
            path = ImageRW.IMAGE_DIR
        else :
            path = ImageRW.TEMP_DIR
        fd = open(path + filename, "wb")
        
        for chunk in file.chunks():
            fd.write(chunk)
        fd.close()
        
        
    
    @staticmethod
    def removeImage(file, in_permanent):
        path = ""
        if in_permanent:
            path = ImageRW.IMAGE_DIR
        else:
            path = ImageRW.TEMP_DIR
            
        try:
            os.remove(path + file) # tries to delete the file
        except OSError:
            pass
    
    @staticmethod
    def convertToTransparent(image):
        pass
        