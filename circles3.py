import numpy as np
import cv2
import sys
import csv

img = cv2.imread('better_test_small.png',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                             param1=50,param2=30,minRadius=0,maxRadius=40)

circles = np.uint16(np.around(circles))


# for i in circles[0,:]:
#   # draw the outer circle
#
#   #i[0] =  x position, i[1] = y position, i[2] = radius
#
#   print(i[0],i[1])
#
#   #THIS THING IS INVERTED (y comes before x)!!!
#   print(cimg[i[1], i[0]])
#
#
#   cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
#   #draw the center of the circle
#   cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)


circles = circles[0]


for i in range(len(circles)):
    # print(circles)
    # print((circles[i][0]), (circles[i][1]))
    # print(cimg[(circles[i][1]),(circles[i][0])])

    #draw the outside of the circle
    cv2.circle(cimg, (circles[i][0], circles[i][1]),circles[i][2],(0,255,0),2)


    # print(sum(cimg[(circles[i][1]),(circles[i][0])]))



    #replace the radius value with the pixel value
    circles[i][2] =   sum(cimg[(circles[i][1]),(circles[i][0])])

    # print(circles[i])





print(circles)

print("iiiii")





#swapping by the x then y then x coordinate

for coordinate in [0,1,0]:
    done = False
    while done is False:
        swap = 0

        for j in range(len(circles) ):
            # print("j = ",j)
            for k in range(j):
                # print("k = ",k)
                if circles[k][coordinate] > circles[k+1][coordinate]:
                    swap = swap+1
                    # print("ck:",circles[k])
                    # print("ck+1:",circles[k+1])

                    for l in range(len(circles[coordinate])):
                        ck = circles[k][l]
                        ckplus = circles[k+1][l]

                        circles[k][l] = ckplus
                        circles[k+1][l] = ck

                    # print("new")
                    # print("ck:", circles[k])
                    # print("ck+1:", circles[k + 1])

        if swap == 0:
            done = True



#Finding thresehold distance between x and y

xRange = np.abs(int(circles[0][0]) - int(circles[-1][0]))
xThres = int(0.1*xRange)

yRange = np.abs(int(circles[0][1]) - int(circles[-1][1]))
yThres = int(0.1*yRange)

#Finding average distance between x and y

xDiff = 0
steps = 0
for i in range(len(circles)-1):
    diff = abs(int(circles[i][0]) - int(circles[i + 1][0]))
    if diff > xThres:
        xDiff = xDiff + diff
        steps = steps+1

xDiff = xDiff/steps


yDiff = 0
steps = 0
for i in range(len(circles)-1):
    diff = abs(int(circles[i][1]) - int(circles[i + 1][1]))
    if diff > yThres:
        yDiff = yDiff + diff
        steps = steps+1

yDiff = yDiff/steps



######CSV

rowLength = 0
with open('data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    #rowLength = len(spamreader[0])
    for row in spamreader: #get length of first row
        rowLength = len(row)
        break


print(circles)

with open('data_out.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #if they have the same y they are same row
    row = []
    for i in range(len(circles)-1):
        print("i is:",i)

        #DEBUG THIS
        if int(abs(int(abs(int(circles[i][1]) -  int(circles[i+1][1])  ))) - yDiff) < yThres:
            #circles that we are adding
            print("circle:",circles[i])
            row.append(str(circles[i][2]))
        print("new row",row)
        spamwriter.writerow(row)




cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()