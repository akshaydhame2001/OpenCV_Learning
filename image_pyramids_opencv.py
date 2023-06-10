import cv2
import numpy as np
img = cv2.imread('lena.jpg')
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i), layer)

layer = gp[5]
cv2.imshow('uppper level Gaussian Pyramid', layer)
lp = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)

# lr1 = cv2.pyrDown(img)
# lr2 = cv2.pyrDown(lr1)
# hr2 = cv2.pyrUp(lr2)

cv2.imshow("Original image", img)
# cv2.imshow("pyrDown 1 image", lr1)
# cv2.imshow("pyrDown 2 image", lr2)
# cv2.imshow("pyrUp 1 image", hr2)
cv2.waitKey(0)
cv2.destroyAllWindows()