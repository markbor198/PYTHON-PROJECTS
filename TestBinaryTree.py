#  File: TestBinaryTree.py

#  Description:A22

#  Student Name:Mark Borjas

#  Student UT EID:mab7886

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 50850

#  Date Created:11/20/20

#  Date Last Modified:11/22/20
import sys

class Node (object):
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
    
  

class Tree (object):
    def __init__(self):
        self.root = None
        
    def insert (self, val):
        newNode = Node(val)

        if (self.root == None):
            self.root = newNode
        else:
            current = self.root
            parent = self.root
            while (current != None):
                parent = current
                if (val < current.data):
                    current = current.lchild
                else:
                    current = current.rchild

            if (val < parent.data):
                parent.lchild = newNode
            else:
                parent.rchild = newNode
  # Returns true if two binary trees are similar
    def is_similar (self, pNode):
        a_node = self.root
        b_node = pNode
        if a_node is None and b_node is None:
            return True
        elif a_node is None or b_node is None:
            return False
        else:
            return self.is_similar_helper(a_node,b_node)
    def is_similar_helper(self,a_node,b_node):
        if a_node is None and b_node is None:
            return True
        elif a_node is None or b_node is None:
            return False
        else:
            return (a_node.data == b_node.data) and \
                   self.is_similar_helper(a_node.rchild,b_node.rchild) and\
                   self.is_similar_helper(a_node.lchild,b_node.lchild)
                   
        

  # Prints out all nodes at the given level
    def print_level (self, level):
        nodes = []
        self.print_helper(level,1,nodes,self.root)
        if len(nodes) == 0:
            return
        else:
            print(nodes)
            

    def print_helper(self,level,current,nodes,other):
        
        if current > level:
            return
        if other == None:
            return
        else:
            if current == level:
                nodes.append(other.data)
                return
            else:
                self.print_helper(level,current+1,nodes,other.lchild)
                self.print_helper(level,current+1,nodes,other.rchild)

  # Returns the height of the tree
    def get_height (self):
        if self.root == None:
            return 0
        else:

            return self.get_height_helper(self.root) -1
    def get_height_helper(self, node):
        if node == None :
            return 0
        else:
            l_height = self.get_height_helper(node.lchild)
            r_height = self.get_height_helper(node.rchild)
        return 1 +  max(l_height,r_height)

  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
    def num_nodes (self):
        if self.root is None:
            return 0
        else:
            #nodes = self.count_nodes(self.root)
            return self.count_nodes(self.root)
    def count_nodes(self, node):
        if node == None:
            return 0
        else:
            return 1 + self.count_nodes(node.lchild) + self.count_nodes(node.rchild)

def main():
    
    
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list (map (int, line)) 	# converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list (map (int, line)) 	# converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list (map (int, line)) 	# converts elements into ints
    #print(tree1_input,tree2_input,tree3_input)
    
    # Test your method is_similar()
    tree1 = Tree()
    for num in tree1_input:
        tree1.insert(num)
    
    tree2 = Tree()
    for num in tree2_input:
        tree2.insert(num)
        
    tree3 = Tree()
    for num in tree3_input:
        tree3.insert(num)
 #Test is_similar for every combination of trees
    print('tree 1 and 2 are similar')
    print(tree1.is_similar(tree2.root))
    
    print('tree 1 and 3 are similar')
    print(tree1.is_similar(tree3.root))
  
    print('different level for 1 and 2')
  #Lets assume that tree1 and tree2 are different
   #print different levels
    for i in range (1, tree1.get_height()+2):
        
        tree1.print_level(i) #assumed to print out on one line
    print()
    print('different level for 1 and 3')
    for i in range(1, tree3.get_height()+2):
        tree3.print_level(i) #assumed to print out on one line

    #tree1.print_level(5) #assumed to print out on one line
    print() #if you need it to ensure the print_levels are on two different lines
    #tree2.print_level(5) #assumed to print out on one line

   #print heights
    print('height')
    print(tree1.get_height())
    print(tree2.get_height())
    print(tree3.get_height())

   #print num_nodes of each tree
    print('num of nodes')
    print(tree1.num_nodes())
    print(tree2.num_nodes())
    print(tree3.num_nodes())
    # Print the various levels of two of the trees that are different

    # Get the height of the two trees that are different

    # Get the total number of nodes a binary search tree

if __name__ == "__main__":
  main()
