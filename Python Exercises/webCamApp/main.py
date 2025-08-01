from itertools import count
from tabnanny import check
import glob
import cv2
import numpy as np
import time

from sendEmail import send_email

video = cv2.VideoCapture(0)
time.sleep(1)
first_frame = None
status_list = []
count = 1

while True:
    status = 0
    ret, frame = video.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)
    #Gausian Grayed Frame
    cv2.imshow("mygauGrayVideo", gray_frame_gau)
    # Regular Frame
    # cv2.imshow("My Video2", frame)

    if first_frame is None:
        first_frame = gray_frame_gau

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)

    thresh_frame = cv2.threshold(delta_frame, 50, 255, cv2.THRESH_BINARY)[1]
    dil_frame =cv2.dilate(thresh_frame, None, iterations=3)
    cv2.imshow("mydilThreshVideo", dil_frame)

    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        if rectangle.any():
            status = 1
            cv2.imwrite(f"./images/{count}.png", frame)
            count = count + 1
            all_images = glob.glob("./images/*.png")
            index = int(len(all_images) / 2)
            print(f"index = {index}")
            # image_with_object = all_images[index]


    status_list.append(status)
    status_list = status_list[-2:]
    if status_list[0] == 1 and status_list[1] == 0:
        send_email()

    print(status_list)

    cv2.imshow("myFrameVideo", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()
