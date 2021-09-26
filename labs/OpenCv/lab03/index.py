import numpy as np
import cv2

#Task (1)
cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('Original',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Task (2.1)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    sobel_horizontal = cv2.Sobel(gray, cv2.CV_16S, 1, 0)
    sobel_vertical = cv2.Sobel(gray, cv2.CV_16S, 0, 1) 
    mat_hor = cv2.convertScaleAbs(sobel_horizontal)
    mat_vert = cv2.convertScaleAbs(sobel_vertical)
    cv2.imshow('Sobel_X',mat_hor)
    cv2.imshow('Sobel_Y',mat_vert)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Task (2.2)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    mat = cv2.convertScaleAbs(laplacian)
    cv2.imshow('Laplacian', mat)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Task (2.3)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 100,200)
    cv2.imshow('Canny', canny)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Task (3)
#Telling about results.

cap.release()
cv2.destroyAllWindows()