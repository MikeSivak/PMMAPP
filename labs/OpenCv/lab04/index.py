import numpy as np
import cv2

#Task (1)
def task_1():
    im = cv2.imread('./images/beatles.jpg')
    cv2.imshow('Original', im)
    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,127,255,0)
    contours, hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(im, contours, -1, (0,255,0), 2, cv2.LINE_AA, hierarchy, 3)
    cv2.imshow("Contours", im)

# #Task (2)
def task_2():
    img = cv2.imread('./images/house.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    cv2.imshow('edges', edges)
    lines = cv2.HoughLines(edges, 1, np.pi / 90, 200)

    for line in lines:
        rho,theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        # x1 stores the rounded off value of (r * cos(theta) - 1000 * sin(theta))
        x1 = int(x0 + 1000 * (-b))
        # y1 stores the rounded off value of (r * sin(theta)+ 1000 * cos(theta))
        y1 = int(y0 + 1000 * (a))
        # x2 stores the rounded off value of (r * cos(theta)+ 1000 * sin(theta))
        x2 = int(x0 - 1000 * (-b))
        # y2 stores the rounded off value of (r * sin(theta)- 1000 * cos(theta))
        y2 = int(y0 - 1000 * (a))
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)


    cv2.imshow('image', img)

#Task (3)
def task_3():
    img = cv2.imread('./images/c.jpg',0)
    img = cv2.medianBlur(img,5)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                                param1=100,param2=50,minRadius=0,maxRadius=0)
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    cv2.imshow('detected circles',cimg)


def main():
    # task_1()
    # cv2.waitKey(0)
    # task_2()
    # cv2.waitKey(0)
    task_3()


main()

cv2.waitKey(0)
cv2.destroyAllWindows()