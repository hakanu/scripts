"""Batch image renamer.

http://hakanu.net
"""
import os

#_BASE_LINK = '/media/h/D/Resimler/_KOMIK/karikatur/'
_BASE_LINK = '/home/h/Desktop/all_karikatur/'

def main():
  print 'Renamer started...'
  counter = 1
  fnames = os.listdir(_BASE_LINK)
  print 'fnames: ', fnames, '\n'
  for filename in fnames:
    print 'filename: ', filename
    new_filename = str(counter) + '.jpg'
    print 'new_filename: ', new_filename
    os.rename(_BASE_LINK + filename, _BASE_LINK + new_filename)
    counter += 1
    if counter % 50 == 0:
      print counter, ' done'
    print '\n'
  print 'Renamer finished...' 
  pass

if __name__ == "__main__":
  main()

