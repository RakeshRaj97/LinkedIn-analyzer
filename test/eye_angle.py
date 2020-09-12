# program to compute eye angle of the linkedin profile picture

"""
__author__: Rakesh Raj Gopala Sai Krishnan
"""

import cv2
import face_recognition
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

image_file = "image.jpeg"
image = face_recognition.load_image_file(image_file)
face_landmarks_list = face_recognition.face_landmarks(image)

for d in face_landmarks_list:
    left_eye = (d['left_eye'])
    right_eye = (d['right_eye'])

x1, y1 = left_eye[0][0], left_eye[0][1] 
x2, y2 = left_eye[3][0], left_eye[3][1]
x_m_left = (x1 + x2)/2
y_m_left = (y1 + y2)/2
print(f"Mid point of left eye: {x_m_left, y_m_left}")
x1, y1 = right_eye[0][0], right_eye[0][1] 
x2, y2 = right_eye[3][0], right_eye[3][1]
x_m_right = (x1 + x2)/2
y_m_right = (y1 + y2)/2
print(f"Mid point of right eye: {x_m_right, y_m_right}")

left_eye_center = [x_m_left, y_m_left]
right_eye_center = [x_m_right, y_m_right]
dy = right_eye_center[1] - left_eye_center[1]
dx = right_eye_center[0] - left_eye_center[0]
angle = np.degrees(np.arctan2(dy, dx)) - 180
angle=abs(angle)
print(angle)

if (angle>0 and angle<5) or (angle>175 and angle<180):
    print("good score")
else:
    print("bad score")
