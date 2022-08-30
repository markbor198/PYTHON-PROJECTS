
#  File: ExpressionTree.py

#  Description: A20

#  Student's Name:Mark Borjas

#  Student's UT EID: mab7886

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E 

#  Unique Number: 58050

#  Date Created: 11/13/20

#  Date Last Modified:11/15/20

import sys
class Stack (object):
    def __init__ (self):
        self.stack = []

  # add an item on the top of the stack
    def push (self, item):
        self.stack.append (item)

  # remove an item from the top of the stack
    def pop (self):
        return self.stack.pop()

  # check the item on the top of the stack
    def peek (self):
        return self.stack[-1]

  # check if the stack is empty
    def is_empty (self):
        return (len(self.stack) == 0)

  # return the number of elements in the stack
    def size (self):
        return (len(self.stack))
    

class Node (object):
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
    

class Tree (object):
    
    def __init__ (self):
        self.root = Node(None)
        
    # take in infix expression and create expression tree   
    def create_tree (self, expr):
        current = self.root
        theStack = Stack()
        operators = ['+', '-', '*', '/', '//', '%', '**']
        tokens = expr.split()

        for item in tokens:
            if item == '(':
                current.lchild = Node(None)
                theStack.push(current)
                current = current.lchild
            elif item in operators:
                current.data = item
                theStack.push(current)
                current.rchild = Node(None)
                current = current.rchild
            elif item not in operators and item != ')':
                current.data = item
                current = theStack.pop()
            elif item == ')':
                if not theStack.is_empty():
                    current = theStack.pop()
                else:
                    break
            
    def evaluate(self, aNode):
        #evaluate operator and operands 
        if aNode.data == '+':
            return self.evaluate(aNode.lchild) + self.evaluate(aNode.rchild)
        
        elif aNode.data == '-':
            return self.evaluate(aNode.lchild) - self.evaluate(aNode.rchild)
        
        elif aNode.data == '*':
            return self.evaluate(aNode.lchild) * self.evaluate(aNode.rchild)
        
        elif aNode.data == '/':
            return self.evaluate(aNode.lchild) / self.evaluate(aNode.rchild)
        
        elif aNode.data == '//':
            return self.evaluate(aNode.lchild) // self.evaluate(aNode.rchild)
        
        elif aNode.data == '%':
            return self.evaluate(aNode.lchild) % self.evaluate(aNode.rchild)
        
        elif aNode.data == '**':
            return self.evaluate(aNode.lchild) ** self.evaluate(aNode.rchild)
        elif aNode.data.isdigit():
            return eval(aNode.data)
        
    #print prefix expression
    def pre_order (self, aNode):
        if aNode != None:
            print(aNode.data, end = ' ')
            self.pre_order(aNode.lchild)
            self.pre_order(aNode.rchild)
            
    #print postfix expression
    def post_order (self, aNode):
        if aNode != None:
            self.post_order(aNode.lchild)
            self.post_order(aNode.rchild)
            print(aNode.data, end = ' ')

def main():

  # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(str(expr))
 
 
  # evaluate the expression and print the result
    print()
    print(expr, " = ", float(tree.evaluate(tree.root)), "\n")
    
  # get the prefix version of the expression and print
    print('Prefix Expression: ', end = ' ')
    tree.pre_order(tree.root)
    print()
    
  # get the postfix version of the expression and print
    print()
    print('Postfix Expression: ',end = ' ')
    tree.post_order(tree.root)
if __name__ == "__main__":
    main()
