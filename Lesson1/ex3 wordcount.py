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

def print_words(filename):
  word_count = create_dict(filename)
  words = sorted(word_count.keys())
  for word in words:
    print (word, word_count[word])


def get_count(word_count_tuple):
  return word_count_tuple[1]


def print_top(filename,number):
  """Prints the "number" top count listing frm a filename"""
  word_count = create_dict(filename)

  # Each item is a (word, count) tuple.
  # Sort them so the big counts are first using key=get_count() to extract count.
  items = sorted(word_count.items(), key=get_count, reverse=True)

  # Print the first 20
  for item in items[:number]:
    print (item[0], item[1])



def main():
  if len(sys.argv) != 3:
    print ('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename,25)
  else:
    print ('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()