import cv2
cam_index = 0
cam = cv2.VideoCapture(cam_index)
while True:
    ret, frame = cam.read()
    if frame is None:
        continue
    cv2.rectangle(frame, (100,100), (500,500), (0,255,0), 2)
    cv2.imshow("Video", frame)
    key = cv2.waitKey(10)
