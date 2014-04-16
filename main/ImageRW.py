import os
from PIL import Image

class ImageRW:
    
    IMAGE_DIR = os.path.dirname(os.path.realpath(__file__)) + "/static/products/"
    TEMP_DIR = os.path.dirname(os.path.realpath(__file__)) + "/static/temp/"
    SUCCESS = 1
    
    
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
    def writeImage(file, permanent, filename): # file is of type UploadedFile
        #this method return the image name
        if file.size > 3000000: # larger than 3 MB
            return ""
        if not (file.name[-4:] == '.jpg' or file.name[-5:] == '.jpeg'): # check format
            return ""
        
        path = ""
        if permanent :
            path = ImageRW.IMAGE_DIR
        else :
            path = ImageRW.TEMP_DIR
        
        try:
            fd = open(path + filename, "wb")
            
            for chunk in file.chunks():
                fd.write(chunk)
            fd.close()
            
            return filename
        except:
            return ""
        
        
    
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
    def convertToTransparent(filename, in_permanent): #this method return the overlay image name
        path = ""
        if in_permanent:
            path = ImageRW.IMAGE_DIR
        else:
            path = ImageRW.TEMP_DIR
        # image_path is assumed to be jpg/jpeg
        im = Image.open(path + filename)
        # convert jpg/jpeg to png
        newpath = path + filename.replace('.jpg', '.png').replace('.jpeg', '.png')
        im.save(newpath, "PNG")
        
        img = Image.open(newpath)
        imga = img.convert("RGBA")
        
        datas = list(imga.getdata()) # get the list of pixels
        
        newData = []
        # loop the list, replace white color wih transparency
        for item in datas:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newData.append((255,255,255,0))
            else:
                newData.append(item)
        
        imga.putdata(newData)
        imga.save(newpath, "PNG")
        
        return filename.replace('.jpg', 'ol.png').replace('.jpeg', 'ol.png') # return the overlay filename
        