
#  File: Radix.py

#  Description: A17

#  Student Name: Mark Borjas

#  Student UT EID: mab7886  

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 80580

#  Date Created: 11/2/20

#  Date Last Modified:11/5/20

import sys

class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue if empty
  def is_empty (self):
    return (len(self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len(self.queue))

# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
  idx_place = 0
  max_length = len(max(a, key = len)) #* int(len(max(a)))
  #print(max_length)
  main_bin = Queue()
  digit_dic = {}
  queue_list = []
  alpha_dic = {chr(i+96):i for i in range(1,27)}
  
  for num in range(10):
    alpha_dic[num] = num
  
  for i in range(10):
    digit_dic[i] = Queue()
    
  for character in range(11,37):
    digit_dic[character] = Queue()
    
  digit_dic[10] = Queue()
 
  for j in a:
    
    while len(j) != max_length:
      j =  j[:] + '*'
  
    main_bin.enqueue(j)
  
  for count in range(1):
    temp_list = []
    
    for strings in range(main_bin.size()):
      digit = main_bin.dequeue()
      try:
        value = str(digit[idx_place])
      except:
        value = str(digit[idx_place])
        
      if str(value) == '*':
        digit_dic[10].enqueue(digit)
        
      elif str(value).isdigit():
        
        digit_dic[int(value)].enqueue(digit)
      else :
        digit_dic[alpha_dic[value]+10].enqueue(digit)
        
    temp_list3 = []
    
    for keys in digit_dic.keys():
      
      if digit_dic[keys].is_empty():
        continue
      
      else:
        for values in range(digit_dic[keys].size()):
          answer = digit_dic[keys].dequeue()
          temp_list3.append(answer)
          main_bin.enqueue(answer)
    
    idx_place += 1
      
  for sort in range(main_bin.size()):
    real_answer = main_bin.dequeue()
    queue_list.append(real_answer.replace("*",""))
  return queue_list


def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)

  '''
  # print word_list
  print (word_list)
  '''
  #print(word_list)
  # use radix sort to sort the word_list
  sorted_list = radix_sort (word_list)

  # print the sorted_list
  print (sorted_list)

if __name__ == "__main__":
  main()

    
