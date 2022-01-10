import cv2
import os
import numpy as np
import time
import glob
import argparse 
import random
import logging
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
    # name='Frames'
    while(1):
      prefix=random.randrange(0, 100, 3)
      name='Frames' + str(prefix)
      if name not in dirs:
        os.mkdir(name)
        break
    self.path=name+'/'
    logfile=name+'.log'
    logging.basicConfig(filename=logfile,
                        format='%(asctime)s %(message)s',
                        filemode='w')
    self.logger = logging.getLogger()
    self.logger.setLevel(logging.DEBUG)

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
    dest=self.path+self.destfol

    if self.dest_Flag_:
      os.mkdir(dest)
      self.dest_Flag_=False

    files=glob.glob(prvLoc+'*.png')
    files.sort()

    for file_ in files:
      folders=file_.split('/')
      folders[1]=self.destfol
      sign='/'
      newfile_=sign.join(folders)
      # newfile_=file_[:-11].replace(self.subfolder,self.destfol)+'/'+file_[11:]
      printl='Moving: ',file_,'->',newfile_
      self.logger.info(printl)
      os.rename(file_,newfile_)
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
    printl='Temps Cleaned...'
    self.logger.info(printl)
    self.merge(self.save)


  def analize(self,rawfolder):
    """
    """
    start_time = time.perf_counter ()
    dirs=os.listdir(rawfolder)
    self.destfol=rawfolder.split('/')[-2]
    
    printl='To process:',dirs
    self.logger.info(printl)
    dirs=[n for n in dirs if n.isnumeric()]
    # dirs.sort()       #ERROR while sorting
    dirs.sort(key = int)
    for dir_ in dirs:
      if dir_.isnumeric():
        filepath=rawfolder+dir_
        rawfile=glob.glob(filepath+'/*.hevc')
        self.branch(rawfile[0])
    
    printl="Process SUCESSFULL ! Completed %d frames"%(self.i)
    self.logger.info(printl)
    end_time = time.perf_counter ()
    
    printl='\n\nexecution time',end_time - start_time, "seconds"
    self.logger.info(printl)

  def branch(self,rawfile):
    """
    """
    
    printl='Reading from:',rawfile
    self.logger.info(printl)
    subpath=list(rawfile.split('/'))
    self.subfolder=subpath[len(subpath)-2]
    self.save=self.path+self.subfolder
    os.mkdir(self.save)
    self.save+='/'
    
    printl='Saving to:',self.save
    self.logger.info(printl)
    self.read(rawfile)
    
  def read(self,rawfile):
    """
    """
    cap = cv2.VideoCapture(rawfile)
    if (cap.isOpened()== False): 
      
      printl="Error opening video stream or file"
      self.logger.info(printl)
    fps = cap.get(cv2.CAP_PROP_FPS)
    pad = '0'
    n = 6
    while(cap.isOpened()):
      ret, frame = cap.read()
      if ret == True:
        frame_name = format(self.i, pad + str(n))+'.png'
        save=self.save+frame_name

        # if rawfile==0:
        #   cv2.imshow('Frame',cv2.flip(frame, 1))
        # else:
        #   # cv2.imshow('Frame',frame)
        
        printl=save,'saving SUCESSFULL !'
        self.logger.info(printl)
        cv2.imwrite(save,frame)
        self.i+=1
        # if cv2.waitKey(25) & 0xFF == ord('q'):
          # break
      else: 
        break

    cap.release()
    # Closes all the frames
    cv2.destroyAllWindows()
    self.clean()