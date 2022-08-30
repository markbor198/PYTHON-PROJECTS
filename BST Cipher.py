#  File: BST_Cipher.py

#  Description: A21

#  Student Name: Mark Borjas

#  Student UT EID: mab7886

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 50850

#  Date Created:11/15/20

#  Date Last Modified:11/17/20
import sys

class Node(object):
    
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
        
class Tree (object):
    
    
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
    def __init__ (self, encrypt_str):
        self.root = None

        for char in encrypt_str:
            
            if ord(char) == 32:
                self.insert(char)
                
            elif (ord(char.lower()) >= 97 and ord(char.lower()) <=122):
                self.insert(char.lower())
                
            else:
                encrypt_str.replace(char, '')
            
        return
    
        

  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
    def insert (self, ch):
        
        new_node = Node (ch)

        if (self.root == None):
            self.root = new_node
            #return
        else:
            current = self.root
            parent = self.root
            while (current != None):
                parent = current
                if (ch == current.data):
                    break
                elif (ch < current.data):
                    current = current.lchild
                else:
                    current = current.rchild

      # found location now insert node
            if (ch < parent.data):
                parent.lchild = new_node
            elif (ch > parent.data):
                parent.rchild = new_node

  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
    def search (self, ch):
        if self.root.data == ch:

            return '*'
        
        strng = ''
        current = self.root
        
        while (current != None):
            if (ch == current.data):
                return strng
            elif (ch < current.data):
                strng += '<'
                current = current.lchild
            elif (ch > current.data):
                strng += '>'
                current = current.rchild
        return strng

  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding 
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
    def traverse (self, st):
        current = self.root
        blank = ''
        for char in st:
            if current != None:
                if char == '*':
                    return current.data
                elif char == '<':
                    current = current.lchild
                elif char == '>':
                    current = current.rchild
            else:
                return blank
            
        return current.data

  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
    def encrypt (self, st):
        st = st.lower()
        encrypt = ''
    
        for char in st:
            if ord(char) == 32 or (ord(char)>= 97 and ord(char)<=122):
                find = self.search(char)
                if find:
                    encrypt += find + '!'
            
        #encrypt = encrypt[:-1]
        return encrypt[:-1]

  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
    def decrypt (self, st):
        st = st.lower()
        decrypt = ''
        decrypt_copy = st.split('!')
        for char in decrypt_copy:
            #print(char)
            decrypt += self.traverse(char)
            
        return decrypt
            

def main():
    
    
  # read encrypt string
    line = sys.stdin.readline()
    encrypt_str = line.strip()

  # create a Tree object
    the_tree = Tree (encrypt_str)

  # read string to be encrypted
    line = sys.stdin.readline()
    str_to_encode = line.strip()

  # print the encryption
    print (the_tree.encrypt(str_to_encode))

  # read the string to be decrypted
    line = sys.stdin.readline()
    str_to_decode = line.strip()
  
  # print the decryption
    print (the_tree.decrypt(str_to_decode))
 
if __name__ == "__main__":
    main()
