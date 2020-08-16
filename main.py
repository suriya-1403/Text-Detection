import cv2
import pytesseract

img = cv2.imread('pic1.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow('Capture',img)
cv2.waitKey(0);
