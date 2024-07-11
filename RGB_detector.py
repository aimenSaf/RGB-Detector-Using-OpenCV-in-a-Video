import cv2
import numpy as np

#code for turning on webcam
capture = cv2.VideoCapture(0)  #0 means webcam video

#loop to get all the frames
while True:
    isTrue, frame = capture.read()
    blank = np.zeros(frame.shape[:2], dtype='uint8')
    cv2.imshow('video', frame)    #Showing the frame captured from video

    b,g,r = cv2.split(frame) 

    mean_blue = cv2.mean(b)
    mean_green = cv2.mean(g)
    mean_red = cv2.mean(r)

    if mean_blue > mean_green and mean_blue > mean_red:
        print('blue')
    if mean_green >mean_blue and mean_green > mean_red:
        print('green')
    if mean_red > mean_blue and mean_red > mean_green:
        print('red')

    if cv2.waitKey(20) & 0xFF==ord('d'):  #if 'd' is pressed, you exit the webcam
        break

capture.release()
cv2.destroyAllWindows()
    
