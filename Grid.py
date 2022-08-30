
#  File: Grid.py

#  Description:A8

#  Student Name:Mark Borjas

#  Student UT EID:mab7886

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 50850

#  Date Created:10/28/20

#  Date Last Modified:10/29/20

import sys

# counts all the possible paths in a grid 
def count_paths (n):
  count = [1 for i in range(n)]
  for i in range(n-1):
      #print('1stloop',count)
      for j in range(1,n):
          count[j] += count[j-1]
          #print('2ndloop',count)
  #print('final',count)
  #print (count[n-1])
  
  return(count[n-1])

# gets the greatest sum of all the paths in the grid
def path_sum (grid, n):
  max_sum = [[0 for i in range(n+1)]for i in range(n+1)]   #int(grid[0][i])
  #print(max_sum)
  for i in range(1,n+1):
    for j in range(1,n+1):
      max_sum[i][j] = (max(int(max_sum[i-1][j]),int(max_sum[i][j-1]))+int(grid[i-1][j-1]))     
  #print (max_sum[n][n])

  return max_sum[n][n]
    
    
  
  

def main():
  # read the dimension of the grid
  line = sys.stdin.readline()
  line = line.strip()
  dim = int (line)

  # create an empty grid
  grid = []

  # populate the grid
  for i in range (dim):
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    row = list (map (int, line))
    grid.append (row)

  '''
  # print the grid
  print (grid)
  '''

  # get the number of paths in the grid and print
  num_paths = count_paths (dim)
  print (num_paths)
  print ()

  # get the maximum path sum and print
  max_path_sum = path_sum (grid, dim)
  print (max_path_sum)

if __name__ == "__main__":
  main()

