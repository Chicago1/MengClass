import cv2

imagem = cv2.imread("better_test.png", cv2.IMREAD_GRAYSCALE)

imagem = cv2.bitwise_not(imagem)

cv2.imshow("Keypoints", imagem)
cv2.waitKey(0)