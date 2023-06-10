import cv2
print(cv2.__version__)
#1,0,-1 channel = RGB, grayscale, orignal with aplha
img = cv2.imread('lena.jpg', 0)
print(img)
cv2.imshow('image', img)
#0xFF mask for 8 bits
k = cv2.waitKey(0) & 0xFF

if k==27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()
