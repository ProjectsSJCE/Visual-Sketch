import cv2
import numpy as np
import scipy.optimize as so
import pymouse
from PIL import Image
from numpy import *
from pylab import *
import time
import math
from datetime import datetime
#import multiprocessing as mp

FRAME_WIDTH = 200
FRAME_HEIGHT = 200
VIDEO_INTERVAL = 20
cam_index = 0
frame_size = 20

ESC = u'\x1b'
BASE_TIME = datetime.now()
mouse = pymouse.PyMouse()

def capture_frames():

    global FRAME_HEIGHT, FRAME_WIDTH, cam_index, frame_size, number        
    cam = cv2.VideoCapture(cam_index)

    red = Image.open("new.jpg")
    red = red.resize((frame_size,frame_size), Image.ANTIALIAS)   
    red = array(red)

    while True:
    # video capture
        ret, frame = cam.read()

        if frame is None:
            continue
        frame = cv2.resize(frame, (FRAME_WIDTH, FRAME_HEIGHT))
        frame = cv2.flip(frame, 1)
        detect_object(frame, red)     
        key = cv2.waitKey(VIDEO_INTERVAL)
        if key == ESC:
            break       

def moveMouse(x, y):

    global BASE_TIME, mouse
    
    elapsed_time = (datetime.now() - BASE_TIME).seconds
    if elapsed_time > 0.5:
        mouse.press(x, y)
        BASE_TIME = elapsed_time
        mouse.release(x, y)            

def detect_object(frame, red):#480*640

    global VIDEO_INTERVAL, frame_size
         
    x_range = len(frame)
    y_range = len(frame[0])
    
    min_std = 100000000000
    i = 0

    while i <= (y_range - frame_size):
        j = 0
        while j <= (x_range - frame_size):
            std = 0    
            cv2.rectangle(frame, (i, j), (i+frame_size, j+frame_size), (0,255,0), 2)
            compare_frame = frame[i:i+frame_size, j:j+frame_size, :]
            std = math.sqrt(sum(sum(sum(abs(compare_frame - red)))))
            if std < min_std:
                min_std = std
                reqx = i
                reqy = j 
            j += frame_size
        i += frame_size
#    img = frame
#    img = cv2.medianBlur(img,5)
#    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

#    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
#                                param1=50,param2=30,minRadius=0,maxRadius=0)

#    circles = np.uint16(np.around(circles))
#    for i in circles[0,:]:
#        # draw the outer circle
#        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
#        # draw the center of the circle
#        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

#    cv2.imshow('detected circles',cimg)
    moveMouse(reqx, reqy)
    cv2.rectangle(frame, (reqy,reqx), (reqy+frame_size,reqx+frame_size), (0,255,0), 2)
    cv2.imshow("Video", frame)
    key = cv2.waitKey(VIDEO_INTERVAL)

def main():
        
    capture_frames()
    
main()
