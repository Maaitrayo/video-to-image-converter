'''
MIT License

Copyright (c) 2021 Maaitrayo Das

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal 
in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

import argparse 
import os
from Editor import extractor as ex

if __name__ == "__main__":
  parser=argparse.ArgumentParser(description="Extraxt and process frames from given dataset for neural network training")
  parser.add_argument('-f','--folder',type=str,help='Parent folder path of the dataset')
  parser.add_argument('-m','--multifolder',type=bool,default=False,help='Manulay input multiple parent folder paths of the dataset')
  parser.add_argument('-a','--autodetect',type=bool,default=False,help='Auto detect multiple parent folder paths of the dataset')
  parser.add_argument('-l','--live',type=str,help='Capture live video input from device camera')
  args=parser.parse_args()
  ex_ob = ex.Extraxtor()
  if args.multifolder:
    folders=args.folder.split(' ')
    for folder in folders:
      print(folder)
  elif args.autodetect:
    folders=os.listdir(args.folder)
    while(1):
      inx=0
      os.system('clear')
      print('---:FOLDERS FOUND:---\nPress: index to remove selection\nPress: -1 to continue\n\n')
      for folder in folders:
        print ('%d.'%(inx+1),folder)
        inx+=1
      # choice=input(':')
      pos=int(input(':'))
      if pos == -1:
        break
      folders.pop(pos-1)
    for folder in folders:
      print('Processing:',args.folder+folder)
      ex_ob.analize(args.folder+folder+'/')

  else:
    ex_ob.analize(args.folder+'/')