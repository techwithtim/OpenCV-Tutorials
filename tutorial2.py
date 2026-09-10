import cv2
import random

img = cv2.imread('assets/logo.jpg', -1)
# for i in range(100):
# 	for j in range(img.shape[1]):
# 		img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
# print(img.shape)
# print(img.shape[0]) # row
# print(img.shape[1]) # column
# print(img.shape[2]) # BGR

# Copy part of image
# tag = img[500:700, 600:900]
# img[100:300, 650:950] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()