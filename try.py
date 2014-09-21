import cv2
import numpy as np
import scipy.optimize as so
import pymouse
from PIL import Image
from numpy import *
from pylab import *
import time

FRAME_WIDTH = 200
FRAME_HEIGHT = 200
VIDEO_INTERVAL = 20
cam_index = 0
frame_size = 30

#BLACK = (0, 0, 0)
#WHITE = (255, 255, 255)
#GREEN = (0, 255, 0)
#RED = (0, 0, 255)
#YELLOW = (30, 255, 255)


def capture_frames():

    global FRAME_HEIGHT, FRAME_WIDTH, cam_index, frame_size, number        
    
    
    cam = cv2.VideoCapture(cam_index)

    
    red = Image.open("red.jpg")
    red = red.resize((frame_size,frame_size), Image.ANTIALIAS)   
    red = array(red)

#    red = cv2.cvtColor(red, cv2.COLOR_BGR2GRAY)

    while True:
    # video capture
        ret, frame = cam.read()

        if frame is None:
            continue
        frame = cv2.resize(frame, (FRAME_WIDTH, FRAME_HEIGHT))
        frame = cv2.flip(frame, 1)

#        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

        detect_object(frame, red)            

#    # fram gray scale
#        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

#        # reverted the grayscaled image
#        frame_gray = cv2.bitwise_not(frame_gray)
#        
#        # do the binary threshold to have a black & white image
#        ret,thresh = cv2.threshold(frame_gray, 200, 255, cv2.THRESH_BINARY)

#        # findContours changes the input so use a copy
#        thresh_copy = np.copy(thresh)




#        contours, hierarchy = cv2.findContours(thresh_copy,cv2.cv.CV_RETR_EXTERNAL,cv2.cv.CV_CHAIN_APPROX_NONE)
#        
#        if len(contours) == 0:
#            continue
#        # draw contours
#        draw_contours = cv2.drawContours(thresh,contours, -1, WHITE, -1)
#        
#        # -------------------------------------------------
#        # max ellipse with NO axis ratio treshold
#        # -------------------------------------------------
#        # find max contour
#        # area_max = 0
#        # for contour in contours:
#        #     area = cv2.contourArea(contour)
#        #     if area > area_max:
#        #         area_max = area
#        #         contour_max = contour

#        # contours with 4 or less points cannot fit an ellipse
#        # if len(contour_max) < 5:
#        #     continue

#        # fit an ellipse within max contour
#        # ellipse = cv2.fitEllipse(contour_max)

#        # -------------------------------------------------
#        # BEGIN max ellipse with axis ratio treshold
#        # -------------------------------------------------
#        # sort contours by area
#        for i in range(0, len(contours)):
#            for j in range(1, len(contours)):
#                area1 = cv2.contourArea(contours[i])
#                area2 = cv2.contourArea(contours[j])
#                if area1 < area2:
#                    contour_tmp = contours[i]
#                    contours[i] = contours[j]
#                    contours[j] = contour_tmp

#        # select the first contour with axis ratio > threshold
#        for contour in contours:
#            if len(contour) < 5:
#                continue
#            e = cv2.fitEllipse(contour)
#            axis_a = min(e[1][0], e[1][1])
#            axis_b = max(e[1][0], e[1][1])
#            try:
#                ratio = axis_a / axis_b
#            except:
#                ratio = 0
#            # print ratio
#            if ratio > 0.6:
#                ellipse = e
#                break

#        if ellipse is None:
#            continue
#        # -------------------------------------------------
#        # max ellipse with axis ratio treshold END
#        # -------------------------------------------------

#        ellipse_centre = (int(ellipse[0][0]), int(ellipse[0][1]))
#        
#        # draw green ellipse around iris and pupil centre      
#        cv2.ellipse(frame, ellipse, GREEN, 2)
#        cv2.circle(frame, ellipse_centre, 2, GREEN, 1)

#        # Display the thresh window
#        cv2.imshow("PUPIL_THRESH_WINDOW", thresh)
#        # display the frame with detected eye
#        cv2.imshow("PUPIL_WINDOW", frame)
#        key = cv2.waitKey(VIDEO_INTERVAL)
    
def detect_object(frame, red):#480*640

    global VIDEO_INTERVAL, frame_size
         
    x_range = len(frame)
    y_range = len(frame[0])
    
    min_std = 100000000000
    i = 0

#    This type of looping is making the iteration damn slow. Any faster way to iterate through numpy arrays? all are numpy arrays BTW
    while i <= (y_range - frame_size):
        j = 0
        while j <= (x_range - frame_size):
            std = 0    

            for iteri in range(frame_size):
                for iterj in range(frame_size):
                    for cur in range(3):
#                        std += (frame[i+iteri][j+iterj][cur] - red[iteri][iterj][cur]) ** 2
                        std += (frame[j+iterj][i+iteri][cur] - red[iterj][iteri][cur]) ** 2
#                        std += (frame[j+iterj][i+iteri] - red[iterj][iteri]) ** 2
            if std < min_std:
                min_std = std
                reqx = i
                reqy = j
            j += frame_size
        i += frame_size
    
    cv2.rectangle(frame, (reqx,reqy), (reqx+frame_size,reqy+frame_size), (0,255,0), 2)
    cv2.imshow("Video", frame)
    key = cv2.waitKey(VIDEO_INTERVAL)

def main():
        
    capture_frames()
    
main()
