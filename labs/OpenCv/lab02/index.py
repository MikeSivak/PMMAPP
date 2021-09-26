import cv2
import numpy as np
import argparse
from skimage.exposure import rescale_intensity
from matplotlib import pyplot as plt

image = cv2.imread('images/world.jpg')

scale_percent = 30                                                          #% from start image size    
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
#Task (1) - 2D Convolution
kernel = np.ones((3,3),np.float32)/9


print(kernel)
def imageCvl(image, kernel):
    result = cv2.filter2D(image, -1, kernel)
    return result

#Task (2) - blur, boxFilter, GaussianBlur и medianBlur functions
def imageBlur(image):
    result = cv2.blur(image,(7,7))
    return result

def imageBoxFilter(image):
    result = cv2.boxFilter(image, -1, (3,3), image, (-1,-1), False, cv2.BORDER_DEFAULT)
    return result

def imageGaussianBlur(image):
    result = cv2.GaussianBlur(image,(3,3),0)
    return result

def imageMedianBlur(image):
    result = cv2.medianBlur(image,7)
    return result

#Task (3) - Erosion and Dilatation
kernel1 = np.ones((5,5), np.uint8)
def erosion(image):
    gray_img = cv2.cvtColor(cv2.resize(image, dim, interpolation = cv2.INTER_AREA), cv2.COLOR_BGR2GRAY)
    (thresh, black_and_white) = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
    result = cv2.erode(black_and_white, kernel1, iterations = 1)
    return result

def dilatation(image):
    gray_img = cv2.cvtColor(cv2.resize(image, dim, interpolation = cv2.INTER_AREA), cv2.COLOR_BGR2GRAY)
    (thresh, black_and_white) = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
    result = cv2.dilate(black_and_white, kernel1, iterations = 1)
    return result

#Task (4) - Finding the boundaries of Canny
def canny(image):
    filtered = imageCvl(image, kernel)
    hsv = cv2.cvtColor(filtered, cv2.COLOR_BGR2HSV)
    # define range of red color in HSV 
    lower_red = np.array([30,150,50]) 
    upper_red = np.array([255,255,180]) 
    mask = cv2.inRange(hsv, lower_red, upper_red)
    # Bitwise-AND mask and original image 
    res = cv2.bitwise_and(filtered,filtered, mask= mask)
    edges = cv2.Canny(filtered,100,200) 
    return edges

#Task (5) - Flattening the histogram
def flatHist(image):
    src = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    dst = cv2.equalizeHist(src)
    # cv2.imshow('Source image', src)
    # cv2.imshow('Equalized Image', dst)

    plt.figure(4)
    plt.subplot(221),plt.imshow(src),plt.title('Original Picture')
    plt.xticks([]), plt.yticks([])
    plt.subplot(222),plt.hist(src.ravel(),256,[0,256]),plt.title('Original Histogram')
    plt.xticks([]), plt.yticks([])

    plt.subplot(223),plt.imshow(dst),plt.title('Aligned Picture')
    plt.xticks([]), plt.yticks([])
    plt.subplot(224),plt.hist(dst.ravel(),256,[0,256]),plt.title('Histo Aligned')
    plt.xticks([]), plt.yticks([])
    plt.gcf().canvas.set_window_title('Fifth task')

    plt.show()

def main():
    #Task (1) -- call imageCvl function
    plt.figure(0)
    cvl = imageCvl(cv2.resize(image, dim, interpolation = cv2.INTER_AREA), kernel)
    plt.subplot(121),plt.imshow(cv2.resize(image, dim, interpolation = cv2.INTER_AREA)),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(cvl),plt.title('Convolution')
    plt.xticks([]), plt.yticks([])
    plt.gcf().canvas.set_window_title('First task')
    plt.show()
    #Task (2) -- call blur, boxFilter, GaussianBlur и medianBlur functions
    plt.figure(1)
    blur = imageBlur(cv2.resize(image, dim, interpolation = cv2.INTER_AREA))
    boxFilter = imageBoxFilter(cv2.resize(image, dim, interpolation = cv2.INTER_AREA))
    gaussianBlur = imageGaussianBlur(cv2.resize(image, dim, interpolation = cv2.INTER_AREA))
    medianBlur = imageMedianBlur(cv2.resize(image, dim, interpolation = cv2.INTER_AREA))
    plt.subplot(221),plt.imshow(blur),plt.title('Blur')
    plt.xticks([]), plt.yticks([])
    plt.subplot(222),plt.imshow(boxFilter),plt.title('Box Filter')
    plt.xticks([]), plt.yticks([])
    plt.subplot(223),plt.imshow(gaussianBlur),plt.title('Gaussian Blur')
    plt.xticks([]), plt.yticks([])
    plt.subplot(224),plt.imshow(medianBlur),plt.title('Median Blur')
    plt.xticks([]), plt.yticks([])
    plt.gcf().canvas.set_window_title('Second task')
    plt.show()
    #Task (3) -- call function erosion
    plt.figure(2)
    erode = erosion(cv2.resize(image, dim, interpolation = cv2.INTER_AREA))
    dilate = dilatation(cv2.resize(image, dim, interpolation = cv2.INTER_AREA))
    plt.subplot(121),plt.imshow(erode),plt.title('Erosion')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(dilate),plt.title('Dilatation')
    plt.xticks([]), plt.yticks([])
    plt.gcf().canvas.set_window_title('Third task')
    plt.show()
    #Task (4) -- call canny function
    plt.figure(3)
    plt.subplot(121),plt.imshow(cv2.resize(image, dim, interpolation = cv2.INTER_AREA)),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    can = canny(cv2.resize(image, dim, interpolation = cv2.INTER_AREA))
    plt.subplot(122),plt.imshow(can),plt.title('Canny Boundaries')
    plt.xticks([]), plt.yticks([])
    plt.gcf().canvas.set_window_title('Fourth task')
    plt.show()
    #Task (5) -- call flatHist function
    flatHist(cv2.resize(image, dim, interpolation = cv2.INTER_AREA))

main()

cv2.waitKey(0)
cv2.destroyAllWindows()