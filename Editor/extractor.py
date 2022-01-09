import cv2
import os
import numpy as np
import glob
import argparse 

class Extraxtor:
  """
  Input: 
        Parent folder path
  Output:
        Single folder named Frames/ conatining 
        all the processed frames from every file 
        in parent folder
  """

  def __init__(self):
    self.i=0
    self.dest_Flag_=True
    dirs=os.listdir()
    if "Frames" not in dirs:
      os.mkdir("Frames")
    self.path='Frames/'

  def merge(self,prvLoc):
    """
    Input:
          Previous location of the 
          child folder conatining processed 
          frames
    Output:
            A single folder with name of the 
            parent folder conating all the frames
    """
    os.system('clear')
    dest='Frames/'+self.destfol

    if self.dest_Flag_:
      os.mkdir(dest)
      self.dest_Flag_=False

    files=glob.glob(prvLoc+'*.png')
    files.sort()

    for file_ in files:
      newfile_=file_[:-11].replace(self.subfolder,self.destfol)+'/'+file_[9:]
      os.rename(file_,newfile_)
      print(file_,'->',newfile_)
    os.rmdir(prvLoc)

  def clean(self):
    """
    Input:
          None
    Output:
          It will remove last 33
          frames of the extraxted 
          frames
    """
    files=os.listdir(self.save)
    files.sort()
    count=33
    while(count>0):
      popfile=files.pop()
      popfile=self.save+popfile
      os.remove(popfile)
      count-=1
    self.i-=33
    print('Cleaned')
    self.merge(self.save)


  def analize(self,rawfolder):
    """
    """
    dirs=os.listdir(rawfolder)
    self.destfol=rawfolder.split('/')[-2]
    dirs.sort()
    for dir_ in dirs:
      if dir_.isnumeric():
        filepath=rawfolder+dir_
        rawfile=glob.glob(filepath+'/*.hevc')
        self.branch(rawfile[0])


  def branch(self,rawfile):
    """
    """
    print('Reading:',rawfile)
    subpath=list(rawfile.split('/'))
    self.subfolder=subpath[len(subpath)-2]
    self.save=self.path+self.subfolder
    os.mkdir(self.save)
    self.save+='/'
    print('Saving:',self.save)
    self.read(rawfile)
    
  def read(self,rawfile):
    """
    """
    cap = cv2.VideoCapture(rawfile)
    if (cap.isOpened()== False): 
      print("Error opening video stream or file")
    fps = cap.get(cv2.CAP_PROP_FPS)
    pad = '0'
    n = 6
    while(cap.isOpened()):
      ret, frame = cap.read()
      if ret == True:
        frame_name = format(self.i, pad + str(n))+'.png'
        save=self.save+frame_name

        if rawfile==0:
          cv2.imshow('Frame',cv2.flip(frame, 1))
        else:
          cv2.imshow('Frame',frame)
        print(save)
        cv2.imwrite(save,frame)
        
        self.i+=1
        if cv2.waitKey(25) & 0xFF == ord('q'):
          break
      else: 
        break

    cap.release()
    # Closes all the frames
    cv2.destroyAllWindows()
    self.clean()