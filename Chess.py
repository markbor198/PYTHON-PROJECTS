
#  File: Chess.py

#  Description:A13

#  Student Name:MARK BORJAS

#  Student UT EID:MAB7886

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 58050

#  Date Created:10/23/20

#  Date Last Modified:

import sys

class Queens (object):
  def __init__ (self, n = 8, count = 0):
    self.board = []
    self.n = n
    self.count = count
    for i in range (self.n):
      row = []
      for j in range (self.n):
        row.append ('*')
      self.board.append (row)

  # print the board
  def print_board (self):
    for i in range (self.n):
      for j in range (self.n):
        print (self.board[i][j], end = ' ')
      print ()
    print ()

  # check if a position on the board is valid
  def is_valid (self, row, col):
    for i in range (self.n):
      if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
        return False
    for i in range (self.n):
      for j in range (self.n):
        row_diff = abs (row - i)
        col_diff = abs (col - j)
        if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
          return False
    return True
    
  # do the recursive backtracking
  def recursive_solve (self, col):
    #count = 0
    if (col == self.n) :
      self.count += 1
     
      return  
    else:
      
      for i in range (self.n):
        if (self.is_valid (i, col)):
          self.board[i][col] = 'Q'
          #count += 1
          if (self.recursive_solve(col + 1)):
            return True
          self.board[i][col] = '*'
      #return False
      return 

  # if the problem has a solution print the board
  def solve (self):
    i = 0
    if self.recursive_solve(i) != 0:
      print(self.count)
    
    
      

def main():
  # read the size of the board
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create a chess board
  game = Queens (n)
  game.solve()
  #print(game.solve())
  # place the queens on the board and count the solutions

  # print the number of solutions
 
if __name__ == "__main__":
  main()

