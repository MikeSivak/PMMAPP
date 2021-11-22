import cv2
img = cv2.imread('./image/hd-wallpapers-4k.jpg')
from matplotlib import pyplot as plt

scale_percent = 30                                                          #% from start image size    
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)        #change image size

cv2.imshow('original', resized)                                             #show original image

gray_img = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

cv2.imshow('gray image', gray_img)

cv2.imwrite('./saved/gray_img.jpg', gray_img)

(thresh, black_and_white) = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)     #convert image to binary 
cv2.imshow('black & white', black_and_white)                                #show binary image

cv2.imwrite('./saved/bnw.jpg', black_and_white)

print(type(img))

# equalizedHist
def flatHist(image):
    src = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    dst = cv2.equalizeHist(src)

    plt.figure(4)
    plt.subplot(221),plt.imshow(src),plt.title('Original Picture')
    plt.xticks([]), plt.yticks([])
    plt.subplot(222),plt.hist(src.ravel(),256,[0,256]),plt.title('Original Histogram')
    plt.xticks([]), plt.yticks([])

    plt.subplot(223),plt.imshow(dst),plt.title('Aligned Picture')
    plt.xticks([]), plt.yticks([])
    plt.subplot(224),plt.hist(dst.ravel(),256,[0,256]),plt.title('Histo Aligned')
    plt.xticks([]), plt.yticks([])
    plt.gcf().canvas.set_window_title('Task 4 - equalizeHist()')

    plt.show()

for i in img:
    print(i)

img2 = cv2.imread('./image/hd-wallpapers-4k.jpg')
resized2 = cv2.resize(img2, dim, interpolation = cv2.INTER_AREA)

flatHist(resized2)

cv2.waitKey(0)
cv2.destroyAllWindows()


