import cv2
import numpy as np
import scipy.optimize as so
import pymouse

FRAME_WIDTH = 500
FRAME_HEIGHT = 500
VIDEO_INTERVAL = 20
cam_index = 0

def capture_frames():

    global FRAME_HEIGHT, FRAME_WIDTH, cam_index, VIDEO_INTERVAL
    cam = cv2.VideoCapture(cam_index)

    while True:
    # video capture
        ret, frame = cam.read()

        if frame is None:
            continue
        
#        frame = cv2.resize(frame, (FRAME_WIDTH, FRAME_HEIGHT))
        cv2.imshow("Video", frame)
        key = cv2.waitKey(VIDEO_INTERVAL)
    
def main():
        
    capture_frames()
    
main()
