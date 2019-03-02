#!/usr/bin/python


#https://github.com/spmallick/learnopencv/blob/master/BlobDetector/blob.py

# Standard imports
import cv2
import numpy as np
import operator

# Read image
im = cv2.imread("better_test.png", cv2.IMREAD_GRAYSCALE)

im = cv2.bitwise_not(im) #inverts the colors



# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 10
params.maxThreshold = 200

# Filter by Area.
params.filterByArea = True
params.minArea = 150

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.1

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.87

# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3:
    detector = cv2.SimpleBlobDetector(params)
else:
    detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs.
keypoints = detector.detect(im)

# Sort them in the order of their distance.
#matches = sorted(keypoints, key = lambda x:x.pt)



# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0, 0, 255),
                                      cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


print(keypoints)


xlist=[]
ylist=[]

for i in range(len(keypoints)):
    xlist.append(round(round((keypoints[i].pt)[0],-1)))
    ylist.append(round((keypoints[i].pt)[1]))





zipped = zip(xlist,ylist)
zipped=list(zipped)
zipped.sort(key=lambda x: x[0])
zipped.sort(key=lambda x: x[1])
zipped.sort(key=lambda x: x[0])

for k in range(len(zipped)):
    zipped[k] = list(zipped[k])



#List of coordinates
print((zipped))

np.savetxt('data.csv', (xlist, ylist), delimiter=',')




# Show blobs
cv2.imshow("Keypoints", im_with_keypoints)
cv2.imwrite('circles_small.png', im_with_keypoints)

cv2.waitKey(0)