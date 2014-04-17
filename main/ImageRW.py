import os
from PIL import Image

class ImageRW:
    
    IMAGE_DIR = os.path.dirname(os.path.realpath(__file__)) + "/static/products/"
    TEMP_DIR = os.path.dirname(os.path.realpath(__file__)) + "/static/temp/"
    SUCCESS = 1
    
    
    def __init__(self):
        pass
    
    @staticmethod
    def readImage(path):  # reads the binary data of an image
        try:
            f = open(ImageRW.IMAGE_DIR + path, "rb")
            byte = f.read()
        except:
            return ''
        return byte
    
    @staticmethod
    def writeImage(file, permanent, filename):  # file is of type UploadedFile
        # this method return the image name
        if file.size > 3000000:  # larger than 3 MB
            return ""
        if not (file.name[-4:].lower() == '.jpg' or file.name[-5:].lower() == '.jpeg'):  # check format
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
            os.remove(path + file)  # tries to delete the file
        except OSError:
            pass
    
    @staticmethod
    def convertToTransparent(filename, in_permanent):  # this method return the overlay image name
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
        
        imga = Image.open(newpath)
        
        imga = imga.convert("RGBA")
        
        pixel = imga.load()
        
        width, height = imga.size
        
        th = 15
        cornerH = 20
        cornerW = 20
        middleW = width / 2
        middleH = height / 2
        # sample four points
        
        pixel1 = pixel[cornerW, cornerH]
        pixel2 = pixel[cornerW, height - cornerH]
        pixel3 = pixel[width - cornerW, cornerH]
        pixel4 = pixel[width - cornerW, height - cornerH]
        pixel5 = pixel[cornerW, height / 2]
        pixel6 = pixel[width - cornerW, height / 2]
        pixel7 = pixel[width / 2, cornerH]
        pixel8 = pixel[width / 2, height - cornerH]
        pixel9 = pixel[cornerW, (middleH + cornerH) / 2]
        pixel10 = pixel[cornerW, (middleH + height - cornerH) / 2]
        pixel11 = pixel[width - cornerW, (middleH + cornerH) / 2]
        pixel12 = pixel[width - cornerW, (middleH + height - cornerH) / 2]
        pixel13 = pixel[(middleW + cornerW) / 2, cornerH]
        pixel14 = pixel[(middleW + width - cornerW) / 2, cornerH]
        pixel15 = pixel[(middleW + cornerW) / 2, height - cornerH]
        pixel16 = pixel[(middleW + width - cornerW) / 2, height - cornerH]
        
        
            
        
        
        
        def checkThreshold(pixelA, pixelB):
            if abs(pixelA[0] - pixelB[0]) <= th and abs(pixelA[1] - pixelB[1]) <= th and abs(pixelA[2] - pixelB[2]) <= th and abs(pixelA[3] - pixelB[3]) <= th:
                return True
        for x in range(width):
            for y in range(height): 
                if checkThreshold(pixel[x, y], pixel1):
                    pixel[x, y] = (255, 255, 255, 0)
                elif checkThreshold(pixel[x, y], pixel2):
                    pixel[x, y] = (255, 255, 255, 0)
                elif checkThreshold(pixel[x, y], pixel3):
                    pixel[x, y] = (255, 255, 255, 0)
                elif checkThreshold(pixel[x, y], pixel4):
                    pixel[x, y] = (255, 255, 255, 0)
                elif checkThreshold(pixel[x, y], pixel5):
                    pixel[x, y] = (255, 255, 255, 0)
                elif checkThreshold(pixel[x, y], pixel6):
                    pixel[x, y] = (255, 255, 255, 0)
                elif checkThreshold(pixel[x, y], pixel7):
                    pixel[x, y] = (255, 255, 255, 0)
                elif checkThreshold(pixel[x, y], pixel8):
                    pixel[x, y] = (255, 255, 255, 0)
                elif checkThreshold(pixel[x, y], pixel9):
                    pixel[x, y] = (255, 255, 255, 0)
                elif checkThreshold(pixel[x, y], pixel10):
                    pixel[x, y] = (255, 255, 255, 0)
                elif checkThreshold(pixel[x, y], pixel11):
                    pixel[x, y] = (255, 255, 255, 0)
                elif checkThreshold(pixel[x, y], pixel12):
                    pixel[x, y] = (255, 255, 255, 0)
                elif checkThreshold(pixel[x, y], pixel13):
                    pixel[x, y] = (255, 255, 255, 0)
                elif checkThreshold(pixel[x, y], pixel14):
                    pixel[x, y] = (255, 255, 255, 0)
                elif checkThreshold(pixel[x, y], pixel15):
                    pixel[x, y] = (255, 255, 255, 0)
                elif checkThreshold(pixel[x, y], pixel16):
                    pixel[x, y] = (255, 255, 255, 0)
            
        
        imga.save(newpath, "PNG")
        
        return filename.replace('.jpg', '.png').replace('.jpeg', '.png')  # return the overlay filename
