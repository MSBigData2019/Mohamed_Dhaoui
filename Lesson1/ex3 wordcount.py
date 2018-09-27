import sys
import os
os.getcwd()

# create dictionary
def create_dict(filepath):
  dict={}
  inputfile= open(filepath, 'r')
  for line in inputfile :
      listwords=line.split(" ")
      for w in listwords:
          w=w.lower()
          w=w.replace("\n"," ")
          if (w in list(dict.keys())):
              dict[w]=dict[w]+1
          else:
              dict.update({w:1})
  return dict


def create_dict(filepath):
  dict={}

dict={'a':1,'b':2}
list(dict.values())
dict.keys
dict.update({'c':2})
