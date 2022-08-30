import sys
#  File: Josephus.py

#  Description: A19

#  Student Name: Mark Borjas

#  Student UT EID: mab7886

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 58050

#  Date Created: 11/9/20

#  Date Last Modified: 11/11/20

class Link(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class CircularList(object):
    
    # Constructor
    def __init__ ( self ):
        self.first = None
      
    
  # Insert an element (value) in the list
    def insert ( self, data):
        new_link = Link(data)
        current = self.first
        if (current == None):
            self.first = new_link
            new_link.next = self.first
            self.first = new_link
            return
        while (current.next != self.first):
            current = current.next
        current.next = new_link
        new_link.next = self.first
        new_link.previous = current

  # Find the link with the given data (value)
    def find ( self, data ):
      current = self.first
      if (current == None):
          return None
      while (current.data != data):
          if (current.next == self.first):
              return None
          else:
              current = current.next
              
      return current
    
      

  # Delete a link with a given data (value)
    def delete ( self, data ):
      current = self.first
      previous = self. first
      if (current == None):
          return None
      while previous.next != current:
          previous = previous.next
      while (current.data != data):
          if (current.next == None):
              return None
          else:
              previous = current
              current = current.next
      if (current == self.first):
          self.first = self.first.next
      else:
          self.first = current.next
      previous.next = current.next
      return current
        

  # Delete the nth link starting from the Link start 
  # Return the next link from the deleted Link
    def delete_after ( self, start, n ):
      current = self.first
      if (self.first == None):
          return None
      while (current.data != start):
          current = current.next
      counter = 1
      while counter != n :
          current = current.next
          counter +=1
      self.delete(current.data)

      #print last person
      print(current.data)
      return current.next

  # Return a string representation of a Circular List
    def __str__ ( self ):
      if self.first == None:
          return "None"
        
      else:
          str_lst = "["
          current = self.first
          
          while current.next != self.first:
              str_lst += (str(current.data) + ", ")
              current = current.next
              
      str_lst += (str(current.data) + "]")
      return str_lst

def main():
  # read number of soldiers
  line = sys.stdin.readline()
  line = line.strip()
  num_soldiers = int (line)
  
  # read the starting number
  line = sys.stdin.readline()
  line = line.strip()
  start_count = int (line)

  # read the elimination number
  line = sys.stdin.readline()
  line = line.strip()
  elim_num = int (line)

  # your code
  answer = CircularList()
  for i in range(1, num_soldiers+1):
      answer.insert(i)
  for i in range(num_soldiers):
      start_count = answer.delete_after(start_count,elim_num)
      start_count = start_count.data
      
if __name__ == "__main__":
  main()
