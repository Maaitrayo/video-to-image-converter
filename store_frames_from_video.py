import cv2
import numpy as np

cap = cv2.VideoCapture('Resources/VID_short.mp4')


if (cap.isOpened()== False): 
  print("Error opening video stream or file")
i=0;

while(cap.isOpened()):
  
  ret, frame = cap.read()
  if ret == True:
    frame_name = str(i)+".png"
    
    cv2.imshow('Frame',frame)    
    cv2.imwrite(frame_name,frame)
    print(frame_name)
      
    i=i+1
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

  
  else: 
    break


cap.release()

# Closes all the frames
cv2.destroyAllWindows()