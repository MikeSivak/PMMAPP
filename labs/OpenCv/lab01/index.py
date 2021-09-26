import cv2
img = cv2.imread('./image/hd-wallpapers-4k.jpg')

scale_percent = 30                                                          #% from start image size    
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)        #change image size

cv2.imshow('original', resized)                                             #show original image

gray_img = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

(thresh, black_and_white) = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)     #convert image to binary 
cv2.imshow('black & white', black_and_white)                                #show binary image
print(type(img))

for i in img:
    print(i)

cv2.waitKey(0)
cv2.destroyAllWindows()


