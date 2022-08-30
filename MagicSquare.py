#  File: MagicSquare.py

#  Description: A13

#  Student Name: Mark Borjas

#  Student UT EID: mab7886

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 50850

#  Date Created: 10/19/20

#  Date Last Modified:10/21/20
import math
# checks if a 1-D list if converted to a 2-D list is magic
# a is 1-D list of integers
# returns True if a is magic and False otherwise

def is_magic ( a ):
    n = int(math.sqrt(len(a)))
    magic_const = n * (n**2 + 1)// 2
    magic_list = []
    mult = 0
    idx = n
    total_rows = 0
    total_col = 0
    total_rdiag = 0
    total_ldiag = 0
    
    while idx  <= n**2:
        magic_list.append(a[mult:idx])
        idx += n
        mult += n
        
    #sum of rows
    for x in range(0,n):
        
        
        if sum(magic_list[x]) == magic_const and sum(magic_list[1]) == magic_const  :
            total_rows += sum(magic_list[x])
    #sum of col
    for row in range(0,n):
        if row >= 1 and magic_const== total_col or magic_const == total_col *n-1  :
            
            total_col = magic_const
            break
        for col in range(0,n):
            
            total_col += magic_list[col][row]
                
            
    
    
    #sum left-right diagonal
    for row in range(1):
        
        for col in range(0,n):
            
            total_rdiag += magic_list[col][col]
        
   

    #sum right-left diagonal
    for row in range(n-1,-1,-n):
        for col in range(n-1,-1,-1):
            
            total_ldiag += magic_list[abs(row-col)][col]
   
    if total_rows == magic_const *n and total_col == magic_const:
        if total_rdiag == magic_const and total_ldiag == magic_const:
        
            '''print('rows',total_rows)
            print('col',total_col)
            print('left to right diag',total_rdiag)
            print('right to left diag',total_ldiag)''' 
            return True
    else:
        
        return False
           
    
        
  
  #return

# this function recursively permutes all magic squares
# a is 1-D list of integers and idx is an index in a
# it stores all 1-D lists that are magic in the list all_magic
def permute ( a, idx, all_magic ):
    
    hi = len(a)
    n = int(math.sqrt(hi))
    real_magic = all_magic[:]
    magic_const = n * (n**2 + 1)// 2
    
    if idx == hi-1  : 
        
        if is_magic(a) and magic_const % a[n+1] ==0 :
            
            all_magic.append(a)
            print(a)
            
        
    else:
        
        for i in range (idx, hi):
            
            a[idx], a[i] = a[i], a[idx]
            if is_magic(a):
                permute (a, idx+1,all_magic)
                
            else:

                
                
                magic_basket = a[:]
            
          
                permute (magic_basket, idx + 1 ,all_magic)
            a[idx], a[i] = a[i], a[idx]
           
def main():
  # read the dimension of the magic square
  in_file = open ('magic.in', 'r')
  line = in_file.readline()
  line = line.strip()
  n = int (line)
  in_file.close()
  #print(n)
  '''
  # check if you read the input correctly
  print (n)
  '''
  #print(n)
  # create an empty list for all magic squares
  all_magic = []
  idx = 0
  # create the 1-D list that has the numbers 1 through n^2
  a = list(range(1,n**2 + 1))
  # generate all magic squares using permutation 
  #print magic squares
  magic_squares = permute( a, idx, all_magic)
  
if __name__ == "__main__":
  main()
