import cv2
import numpy
import pytesseract

screen = cv2.imread('pic2.jpg')
screen = cv2.cvtColor(screen,cv2.COLOR_BGR2RGB)

#print(pytesseract.image_to_boxes(screen))
"""height,width,_=screen.shape
config=r'--oem 2 --psm 6 outputbase digits'
box=pytesseract.image_to_boxes(screen,config=config)
for b in box.splitlines():
    b=b.split(' ')
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(screen,(x,height-y),(w,height-h),(0,0,255),1)
    cv2.putText(screen,b[0],(x,height-y+20),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),1)"""

height,width,_=screen.shape
box=pytesseract.image_to_data(screen)
print(box)
for x,b in enumerate(box.splitlines()):
    if x!=0:
        b=b.split()
        print(b)
        if(len(b)==12):
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(screen,(x,y),(w+x,h+y),(0,0,255),1)
            cv2.putText(screen,b[11],(x,height-y+20),cv2.FONT_HERSHEY_SIMPLEX,1,(50,50,255),1)


cv2.imshow('Capture',screen)
cv2.waitKey(0);
