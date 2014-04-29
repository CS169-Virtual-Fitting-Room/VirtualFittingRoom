import os
from PIL import Image, ImageMath

class ImageRW:
    
    IMAGE_DIR = os.path.dirname(os.path.realpath(__file__)) + "/static/products/"
    TEMP_DIR = os.path.dirname(os.path.realpath(__file__)) + "/static/temp/"
    PROFILE_DIR = os.path.dirname(os.path.realpath(__file__)) + "/static/profile/"
    SUCCESS = 1
    
    
    @staticmethod
    def readImage(path):  # reads the binary data of an image
        try:
            f = open(ImageRW.IMAGE_DIR + path, "rb")
            byte = f.read()
        except:
            return ''
        return byte
    
    @staticmethod
    def writeImage(file, permanent, filename, profile = False):  # file is of type UploadedFile
        # this method return the image name
        if file.size > 3000000:  # larger than 3 MB
            return ""
        if not (file.name[-4:].lower() == '.jpg' or file.name[-5:].lower() == '.jpeg'):  # check format
            return ""
        
        path = ""
        if profile:
            path = ImageRW.PROFILE_DIR
        elif permanent :
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
    def removeImage(file, in_permanent, debug = False):
        path = ""
        if in_permanent:
            path = ImageRW.IMAGE_DIR
        else:
            path = ImageRW.TEMP_DIR
            
        try:
            os.remove(path + file)  # tries to delete the file
        except OSError:
            if debug:             
                return True
            else:
                pass
    
    @staticmethod
    def Process(filename, in_permanent, category):  # this method return the overlay image name
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
         
         
        # try to trim the bottom and top if it is hat
        if (category == "hats"):
            thTrim = 5
            tip = height
            bottom = 0
            left = width
            right = 0
            # trim up first
            for x in range(width):
                y = 0
                foundObj = False
                while (not foundObj) and y < height:
                    if pixel[x, y][3] != 0:
                        foundObj = True
                        if y < tip:
                            tip = y
                    y += 1
        
            for x in range(width):
                y = height - 1
                foundObj = False
                while (not foundObj) and y >= 0:
                    if pixel[x, y][3] != 0:
                        foundObj = True
                        if y > bottom:
                            bottom = y
                    y -= 1
            for y in range(height):
                x = 0
                foundObj = False
                while (not foundObj) and x < width:
                    if pixel[x, y][3] != 0:
                        foundObj = True
                        if x < left:
                            left = x
                    x += 1
        
            for y in range(height):
                x = width - 1
                foundObj = False
                while (not foundObj) and x >= 0:
                    if pixel[x, y][3] != 0:
                        foundObj = True
                        if x > right:
                            right = x
                    x -= 1
            
            if (tip - thTrim < height and bottom + thTrim >= 0 and left - thTrim >=0 and right + thTrim < width):
                imga = imga.crop((left - thTrim, tip - thTrim, right + thTrim, bottom + thTrim))
            
            else:
                imga = imga.crop((left, tip, right, bottom))
                
        # try to trim for headphones
        elif (category == "headphones"):
            # find ear to ear distance
            bottomsLeft = []
            bottomsRight = []
            tip = height
            middle = 0
            # find tip first
            
            for x in range(width):
                y = 0
                foundObj = False
                while (not foundObj) and y < height:
                    if pixel[x, y][3] != 0:
                        if y < tip:
                            tip = y
                            middle = x
                            foundObj = True
                    y += 1

            for x in range(0, middle):
                for y in reversed(range(height)):
                    if pixel[x,y][3] != 0:
                        bottomsLeft.append((x, y))
                        break
                    
            for x in reversed(range(middle, width)):
                for y in reversed(range(height)):
                    if pixel[x,y][3] != 0:
                        bottomsRight.append((x, y))
                        break
            th = 20
            thTrim = 5
            # sort it for now, ~1000 pixels isn't that much??
            bottomsLeft = sorted(bottomsLeft, key=lambda x: x[1], reverse = True)
            bottomsRight = sorted(bottomsRight, key=lambda x: x[1], reverse = True)
            
            found = False
            i = j = 0
            bottom = 0
            leftEar = rightEar = 0
            while not found:
                if abs(bottomsLeft[i][1] - bottomsRight[j][1]) <= th:
                    found = True
                    bottom = max(bottomsLeft[i][1], bottomsRight[j][1])
                    leftEar = bottomsLeft[i][0]
                    rightEar = bottomsRight[j][0]
                else:
                    if bottomsLeft[i][1] > bottomsRight[j][1]:
                        i += 1
                    else:
                        j += 1
                        
            # now crop the image
            if (tip - thTrim < height and bottom + thTrim >= 0):
                imga = imga.crop((0, tip - thTrim, width, bottom + thTrim))
            
            else:
                imga = imga.crop((0, tip, width, bottom))    
            
            # find ear to ear distance           
            new_width, new_height = imga.size
            lefttip = new_width
            righttip = 0
            newpixel = imga.load()
            
            for y in reversed(range(new_height)):
                for x in reversed(range(leftEar)):
                    if newpixel[x, y][3] == 0:
                        if x < lefttip:
                            lefttip = x
                        break
            
            for y in reversed(range(new_height)):
                for x in range(rightEar, new_width):          
                    if newpixel[x, y][3] == 0:
                        if x > righttip:
                            righttip = x
                        break
            #new_width = width + int(round(xshift))
            imga = imga.transform((new_width, new_height), Image.QUAD,
                    (0,0, lefttip, new_height, righttip ,new_height,new_width,0), Image.BILINEAR)
        
        # process glasses
        elif category == "glasses":
            thTrim = 5
            tip = height
            bottom = 0
            left = width
            right = 0
            # trim up first
            for x in range(width):
                y = 0
                foundObj = False
                while (not foundObj) and y < height:
                    if pixel[x, y][3] != 0:
                        foundObj = True
                        if y < tip:
                            tip = y
                    y += 1
        
            for x in range(width):
                y = height - 1
                foundObj = False
                while (not foundObj) and y >= 0:
                    if pixel[x, y][3] != 0:
                        foundObj = True
                        if y > bottom:
                            bottom = y
                    y -= 1
            for y in range(height):
                x = 0
                foundObj = False
                while (not foundObj) and x < width:
                    if pixel[x, y][3] != 0:
                        foundObj = True
                        if x < left:
                            left = x
                    x += 1
        
            for y in range(height):
                x = width - 1
                foundObj = False
                while (not foundObj) and x >= 0:
                    if pixel[x, y][3] != 0:
                        foundObj = True
                        if x > right:
                            right = x
                    x -= 1
            
            if (tip - thTrim < height and bottom + thTrim >= 0 and left - thTrim >=0 and right + thTrim < width):
                imga = imga.crop((left - thTrim, tip - thTrim, right + thTrim, bottom + thTrim))
            
            else:
                imga = imga.crop((left, tip, right, bottom))
            
        imga.thumbnail((600,600), Image.ANTIALIAS) # set the max size
        imga.save(newpath, "PNG")
        
        return filename.replace('.jpg', '.png').replace('.jpeg', '.png')  # return the overlay filename
