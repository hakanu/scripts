"""Resize images in a folder using imagemagick command line tools.

http://hakanu.net
"""

import glob
import os

def main():
  print 'Started'
  images = glob.glob("/home/h/Desktop/all_karikatur_resized/*.jpg")
  counter = 0
  for image in images:
    print 'Processing: ', image
    index = image[image.rfind('/') + 1:image.rfind('.jpg')]
    print 'index: ', index
    os.system("convert " + index + ".jpg  -resize 128x128 resize_128_" + index + ".jpg")
    counter += 1
    if counter % 100 == 0:
      print 'Completed: ', counter
    print '\n'

main()
