'''MIT License

Copyright (c) 2021 Maaitrayo Das

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal 
in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.'''


import cv2
import os
import numpy as np

class Extraxtor:
  def __init__(self):
    os.mkdir("Frames")
    self.path='Frames/'
  def analize(self,rawfile):  
    cap = cv2.VideoCapture(rawfile)
    if (cap.isOpened()== False): 
      print("Error opening video stream or file")
    i=0
    pad = '0'
    n = 6
    while(cap.isOpened()):
      
      ret, frame = cap.read()
      if ret == True:
        frame_name = format(i, pad + str(n))+'.png'
        path+=frame_name

        
        cv2.imshow('Frame',frame)    
        cv2.imwrite(path,frame)
        print(frame_name)
          
        i=i+1
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
          break

      
      else: 
        break
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()

if __name__ == '__main__':
  extract=Extraxtor()
  extract.analize('Video.mp4')

