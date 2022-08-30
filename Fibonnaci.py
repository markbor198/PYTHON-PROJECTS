# File: Fibonacci.py

# Description: 

# Student's Name:Mark Borjas

# Student's UT EID:mab7886

# Partner's Name:

# Partner's UT EID:

# Course Name: CS 313E

# Unique Number:50850

# Date Created:10/11/2020

# Date Last Modified:10/12/2020

import sys

# Input: n a positive integer
# Output: a bit string
def f ( n ):
    if ( n == 0 ) or ( n == 1 ):
        return str(n)
    else:
        return f (n - 1) + f(n - 2) 
    


# Input: s and p are bit strings
# Output: an integer that is the number of times p occurs in s
def count_overlap (s, p):
    count = 0
    x = 0
    
    while x < len(s):
        
        if (s[x:len(p)+x]) == p :
            count += 1
            x += len(p)-1
        else:
            x += 1
            
        
    
    return count

       
            
        

def main():
  # read n and p from standard input
  n = sys.stdin.readline()
  n = int (n.strip())
  p = sys.stdin.readline()
  p = p.strip()

  # compute the bit string f(n)
  s = f(n)
  # determine the number of occurrences of p in f(n)
  count = count_overlap(s,p)
  # print the number of occurrences of p in f(n)
  print(count)
if __name__ == "__main__":
  main()

