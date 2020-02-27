# This is the problem for First technical round for the role of Computer Vision Engineer at Vectorly
# More details at https://www.linkedin.com/jobs/view/1629909785/
#
# Write a function which will segment and extract the text overlay "Bart & Homer's EXCELLENT Adventure" 
# Input image is at https://vectorly.io/demo/simpsons_frame0.png
# Output : Image with only the overlay visible and everything else white
# 
# Note that you don't need to extract the text, the output is an image with only 
# the overlay visible and everything else (background) white
#
# You can use the snipped below (in python) to get started if you like 
# Python is not required but is preferred. You are free to use any libraries or any language


#####################
import cv2
import numpy as np
from PIL import Image

def getTextOverlay(input_image):

    greyScale = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    
    kernel = np.ones((5,5), np.uint8)
    inverted = cv2.bitwise_not(greyScale)
    erosion = cv2.erode(inverted, kernel, iterations = 2) #remove the extra lines 
    dilation = cv2.dilate(erosion,kernel,iterations = 3)
    # thresh = cv2.adaptiveThreshold(dilation, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,8)
    img = dilation
    np_img = np.array(img)

    # naive dilation, if pixel value is less than 225, convert to black    
    x ,y = np_img.shape

    for i in range(0, x):
        for j in range(0, y):
            if(np_img[i][j] < 225):
                np_img[i][j] = 0

    return np_img

if __name__ == '__main__':
    image = cv2.imread('simpsons_frame0.png')
    output = getTextOverlay(image)
    cv2.imwrite('simpons_text.png', output)
#####################