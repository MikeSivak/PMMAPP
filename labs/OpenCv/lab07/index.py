
from __future__ import print_function
import cv2 as cv
import argparse
parser = argparse.ArgumentParser(description='This program shows how to use background subtraction methods provided by \
                                              OpenCV. You can process both videos and images.')
parser.add_argument('--input', type=str, help='Path to a video or a sequence of image.', default='slow_traffic_small.mp4')
parser.add_argument('--algo', type=str, help='Background subtraction method (KNN, MOG2).', default='MOG2')
args = parser.parse_args()
if args.algo == 'MOG2':
    backSub = cv.createBackgroundSubtractorMOG2()
else:
    backSub = cv.createBackgroundSubtractorKNN()
capture = cv.VideoCapture(cv.samples.findFileOrKeep(args.input))
if not capture.isOpened():
    print('Unable to open: ' + args.input)
    exit(0)
while True:
    ret, frame = capture.read()
    if frame is None:
        break
    
    fgMask = backSub.apply(frame)
    
    
    cv.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
    cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
               cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
    
    
    cv.imshow('Frame', frame)
    cv.imshow('FG Mask', fgMask)
    
    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break

# Task (1 or 3???)

import cv2  # импорт модуля cv2

# cv2.VideoCapture("видеофайл.mp4"); вывод кадров из видео файла
cap = cv2.VideoCapture(0)  # видео поток с веб камеры

cap.set(3, 1280)  # установка размера окна
cap.set(4, 700)

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():  # метод isOpened() выводит статус видеопотока

    # нахождение разницы двух кадров, которая проявляется лишь при изменении одного из них, т.е. с этого момента наша программа реагирует на любое движение.
    diff = cv2.absdiff(frame1, frame2)
    # diff = cv2.absdiff(fgMask1, fgMask2)

    # перевод кадров в черно-белую градацию
    gray = cv2.cvtColor(diff, cv2 .COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)  # фильтрация лишних контуров

    # метод для выделения кромки объекта белым цветом
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    # данный метод противоположен методу erosion(), т.е. эрозии объекта, и расширяет выделенную на предыдущем этапе область
    dilated = cv2.dilate(thresh, None, iterations=3)

    # нахождение массива контурных точек
    сontours, _ = cv2.findContours(
        dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in сontours:
        # преобразование массива из предыдущего этапа в кортеж из четырех координат
        (x, y, w, h) = cv2.boundingRect(contour)

        # метод contourArea() по заданным contour точкам, здесь кортежу, вычисляет площадь зафиксированного объекта в каждый момент времени, это можно проверить
        print(cv2.contourArea(contour))

        # условие при котором площадь выделенного объекта меньше 700 px
        if cv2.contourArea(contour) < 700:
            continue
        # получение прямоугольника из точек кортежа
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame1, "Status: {}".format("Motion was detected"), (10, 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3, cv2.LINE_AA)  # вставляем текст

    # cv2.drawContours(frame1, сontours, -1, (0, 255, 0), 2) также можно было просто нарисовать контур объекта

    cv2.imshow("Task 1", frame1)
    frame1 = frame2  #
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break


cap.release()
cv2.destroyAllWindows()

# Task (2) - calcOpticalFlowPyrLK()
import numpy as np
import cv2 as cv
import argparse
parser = argparse.ArgumentParser(description='This sample demonstrates Lucas-Kanade Optical Flow calculation. \
                                              The example file can be downloaded from: \
                                              https://www.bogotobogo.com/python/OpenCV_Python/images/mean_shift_tracking/slow_traffic_small.mp4')
# parser.add_argument('image', type=str, help='path to image file')
# args = parser.parse_args()
# cap = cv.VideoCapture(args.image)

cap = cv.VideoCapture("slow_traffic_small.mp4")
# params for ShiTomasi corner detection
feature_params = dict(maxCorners=100,
                      qualityLevel=0.3,
                      minDistance=7,
                      blockSize=7)
# Parameters for lucas kanade optical flow
lk_params = dict(winSize=(15, 15),
                 maxLevel=2,
                 criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))
# Create some random colors
color = np.random.randint(0, 255, (100, 3))
# Take first frame and find corners in it
ret, old_frame = cap.read()
old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
p0 = cv.goodFeaturesToTrack(old_gray, mask=None, **feature_params)
# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)
while(1):
    ret, frame = cap.read()
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # calculate optical flow
    p1, st, err = cv.calcOpticalFlowPyrLK(
        old_gray, frame_gray, p0, None, **lk_params)
    # Select good points
    if p1 is not None:
        good_new = p1[st == 1]
        good_old = p0[st == 1]
    # draw the tracks
    for i, (new, old) in enumerate(zip(good_new, good_old)):
        a, b = new.ravel()
        c, d = old.ravel()
        mask = cv.line(mask, (int(a), int(b)),
                       (int(c), int(d)), color[i].tolist(), 2)
        frame = cv.circle(frame, (int(a), int(b)), 5, color[i].tolist(), -1)
    img = cv.add(frame, mask)
    cv.imshow('Task 2', img)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
    # Now update the previous frame and previous points
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1, 1, 2)
