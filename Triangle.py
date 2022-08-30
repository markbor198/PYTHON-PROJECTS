#  File: Triangle.py

#  Description:A15

#  Student Name:Mark Borjas

#  Student UT EID:mab7886

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 50850

#  Date Created: 10/25/20

#  Date Last Modified:10/28/20

import sys
import math
from timeit import timeit

# returns the greatest path sum using exhaustive search
def brute_force_helper(grid, r, i,  path_sum,path_list):

  if i  == len(grid)-1 :
    path_sum += grid[i][r]
    path_list.append(path_sum)
    
    return path_sum
  else:
  
    return max(brute_force_helper(grid, r+1, i+1, path_sum +grid[i][r] , path_list),brute_force_helper(grid, r, i+1, path_sum+ grid[i][r]   ,path_list))
    

def brute_force (grid):
  path_list = []
  get_path = brute_force_helper(grid,0,0,0,path_list)
  return path_list


# returns the greatest path sum using greedy approach
def greedy (grid):
  r = 0
  path_sum = 0
  path_sum += grid[0][0]
  for i in  range(len(grid)-1) :
    
    if grid[i+1][r+1] > grid[i+1][r]:
      path_sum += grid[i+1][r+1]
      r += 1
    else:
      path_sum += grid[i+1][r]
  return path_sum  
 
# returns the greatest path sum using divide and conquer (recursive) approach
def dc_helper(grid,i,r):
  if i  == len(grid)-1 :
    return grid[i][r]
  else:
    return grid[i][r]+ max(dc_helper(grid, i+1, r+1) ,dc_helper(grid, i+1, r))
    
def divide_conquer (grid):
  get_path = dc_helper(grid,0,0)
  return get_path


# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
  n = len(grid)
  path_list = grid[:]
  
  
  for i in range(len(path_list)-1,0,-1):
                 
          
    for j in range(len(path_list[i])-1):
      if path_list[i][j] < path_list[i][j+1]:
        path_list[i-1][j] += path_list[i][j+1]
      else:
        path_list[i-1][j] += path_list[i][j]
  #print(path_list)      
  return path_list[0][0]
                 
        
        
      

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    row = line.split()
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]

  return grid 


def main ():
  # read triangular grid from file
  grid = read_file()
  
  
  #print_tri(grid)
  # output greatest path from exhaustive search
  print('The greatest path sum through exhaustive search is')
  print(max(brute_force(grid)))
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  # print time taken using exhaustive search
  print('The time taken for exhaustive search in seconds is')
  print(times)
  #print(brute_force(grid))
  print('')
  # output greatest path from greedy approach
  print('The greatest path sum through greedy approach is')
  print(greedy(grid))
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  # print time taken using greedy approach
  print('The time taken for greedy approach in seconds is')
  print(times)

  print('')
  # output greatest path from divide-and-conquer approach
  print('The greatest path sum through divide-and-conquer approach is')
  print(divide_conquer(grid))
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach
  print('The time taken for divide-and-conquer approach in seconds is')
  print(times)

  print('')
  # output greatest path from dynamic programming
  print('The greatest path sum through dynamic programming is')
  print(dynamic_prog(grid))
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10

  #print('')
  # print time taken using dynamic programming
  print('The time taken for dynamic programming in seconds is')
  print(times)
if __name__ == "__main__":
  main()
