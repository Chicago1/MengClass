import cv2
import numpy as np

img = cv2.imread('better_test.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)
# Threshold for an optimal value, it may vary depending on the image.

img[dst>0.001*dst.max()]=[0,0,255]

img[dst<0.001*dst.max()]=[0,0,0]

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()




#TODO: finds the outline of the box with dots
#creates grid pattern of expected points
#check if there are dots or not