import cv2
import numpy as np

cap = cv2.VideoCapture("test2.mp4")

#get the video properties
fps = cap.get(cv2.CAP_PROP_FPS)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

pixels = (frame_width, frame_height)

#create videowriter object
fourcc = cv2.VideoWriter_fourcc(*'avc1')  # H.264 code

out = cv2.VideoWriter('output.mp4', fourcc, fps, pixels, isColor=False)

while (cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    out.write(gray)

cap.release()
out.release()
