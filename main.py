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
import argparse 

class Extraxtor:
  def __init__(self):
    dirs=os.listdir()
    if "Frames" not in dirs:
      os.mkdir("Frames")
    self.path='Frames/'

  def clean(self):
    print(os.getcwd())
    files=os.listdir('Frames')
    files.sort()
    count=33
    while(count>0):
      popfile=files.pop()
      popfile='Frames/'+popfile
      os.remove(popfile)
      count-=1

  def analize(self,rawfile):
    subpath=list(rawfile.split('/'))
    self.subfolder=subpath[len(subpath)-2]
    self.path=self.path+self.subfolder
    print(self.path)
    os.mkdir(self.path)
    self.path+='/'
    self.read(rawfile)  
    
  def read(self,rawfile):
    cap = cv2.VideoCapture(rawfile)
    if (cap.isOpened()== False): 
      print("Error opening video stream or file")
    fps = cap.get(cv2.CAP_PROP_FPS)
    i=0
    pad = '0'
    n = 6
    while(cap.isOpened()):
      ret, frame = cap.read()
      if ret == True:
        frame_name = format(i, pad + str(n))+'.png'
        save=self.path+frame_name

        if rawfile==0:
          # Flip for selfie view
          cv2.imshow('Frame',cv2.flip(frame, 1))
        else:
          cv2.imshow('Frame',frame)
        cv2.imwrite(save,frame)
        # print(frame_name)
        i=i+1
        if cv2.waitKey(25) & 0xFF == ord('q'):
          break
      else: 
        # print("Error! Can't read data")
        break
    cap.release()
    # Closes all the frames
    cv2.destroyAllWindows()
    self.clean()

if __name__ == '__main__':
  extract=Extraxtor()
  path='/Users/alpha/Downloads/Chunk_10_5/99c94dc769b5d96e_2018-11-16--10-00-42/32/video.hevc'
  # path=list(path.split('/'))
  # print(path[len(path)-2])
  extract.analize('/Users/alpha/Downloads/Chunk_10_5/99c94dc769b5d96e_2018-11-16--10-00-42/32/video.hevc')
  # extract.analize('/Users/alpha/Downloads/Flower.mov')


