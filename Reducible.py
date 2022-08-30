#  File: Reducible.py

#  Description: A16

#  Student Name: Mark Borjas

#  Student UT EID: mab7886  

#  Partner Name:

#  Partner UT EID: mab7886

#  Course Name: CS 313E

#  Unique Number: 50850

#  Date Created:10/31/20

#  Date Last Modified:11/2/20


# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
  if (n == 1):
    return False

  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True

# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word (s, size):
  hash_idx = 0
  for j in range (len(s)):
    letter = ord(s[j]) - 96
    hash_idx = (hash_idx * 26 + letter) % size
  return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):
    hash_idx = 0
    for j in range (len(s)):
        letter = ord(s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % const
    
    step_size = const - (hash_idx % const)
    return step_size

# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
  idx = hash_word(s,len(hash_table))
  if hash_table[idx] != " ":
    step_idx = step_size(s,13)
    i = 1
    while hash_table[(idx + step_idx * i) % len(hash_table)] != " ":
      i += 1

    hash_table[(idx + step_idx * i) % len(hash_table)] = s
  else:
    hash_table[idx] = s
    

# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):
    
    idx = hash_word(s,len(hash_table))
    
    if hash_table[idx] == s:
      return True
    
    if hash_table[idx] != " ":
      step_idx = step_size(s,13)
      i = 1
      while (hash_table[(idx + step_idx * i) % len(hash_table)] != " "):
        if hash_table[(idx + step_idx * i) % len(hash_table)] == s:
          return True
        i += 1

    return False
    
# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
  if find_word(s,hash_memo):
    return True
  if len(s) == 1:
    #print(s)
    return s == "a" or s == "i" or s =="o"
    
  for sub_word in is_reducible_helper(s,hash_table):
    #print(sub_word)
    #if len(sub_word) == 1:
      #print(sub_word,s)
    if is_reducible(sub_word,hash_table,hash_memo):
      #print(sub_word)
      insert_word(sub_word,hash_memo)
      return True
  else:
    return False
    
    
def is_reducible_helper(s, hash_table):
  reducible_permu = []
  #print('word',s)
  for i in range(len(s)):
    sub_word =  s[:i] + s[i+1:]
    if find_word(sub_word,hash_table):
      #print(sub_word)
      reducible_permu.append(sub_word)
    #print(reducible_permu)
    #print(sub_word)
  return reducible_permu
def is_reducible_sec_helper(s,hash_table):
  pass
# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):
    pass

def main():
    
  # create an empty word_list
    word_list=[]
  # open the file words.txt
    words_txt = open('words.txt','r')
  # read words from words.txt and append to word_list
    #line = words_txt.readline()
    for i in words_txt:
        #print(i)
        word_list.append(i.strip())
        
    words_txt.close()
    #print(word_list[0],word_list[-1])
    word_list.append("a")
    word_list.append("i")
    word_list.append("o")
    #print(len(word_list))
    #print(word_list[-1])
    words_len = len(word_list)
        
  # close file words.txt

  # find length of word_list

  # determine prime number N that is greater than twice
  # the length of the word_list
    N = words_len *2
    while is_prime(N) != True:
        N += 1
    #print(N)
    
  # create an empty hash_list
    hash_list = []
  # populate the hash_list with N blank strings
    for i in range(N):
        hash_list.append(" ")
    #print(hash_list)
  # hash each word in word_list into hash_list
  # for collisions use double hashing 
    for word in word_list:
        #print(word)
        insert_word(word,hash_list)
        #print('x')
    #print('out')
    #print(hash_list)
    hash_memo = []
  # create an empty hash_memo of size M
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than 
  # 0.2 * size of word_list
    M = int(0.2 * len(word_list))
    
    while is_prime(M) != True:
        M += 1
    #print(M)
  # populate the hash_memo with M blank strings
    for i in range(M):
        hash_memo.append(" ")
        #print('x')
  # create an empty list reducible_words
    reducible_words = []
  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
    #print(hash_memo[-1])
    #print(hash_list[-1])
    for word in word_list:
      if len(word) == 10:
        #print('word',word)
        if is_reducible(word,hash_list,hash_memo) == True:
          print(word)
  

if __name__ == "__main__":
  main()
