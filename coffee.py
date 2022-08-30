import time

# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
    p = 0
    total = 0
    term_num = 0
    term = v // k**p
    while v//k**p !=  0:
        total += v//k**p
        p +=1 
    return total
    
    
    #for i in range(1,1000000):
       

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
    for i in range(1,n):
        if sum_series(i,k) >= n and sum_series(i+1,k) > n \
           and sum_series(i-1,k) < n:
            return i
    
        
# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
    lo = 1
    hi = n
    while lo <= hi:
        mid = sum_series(lo,k)
        if n > mid:
            lo += 1
        elif mid >= n and sum_series(lo+1,k) > n and sum_series(lo-1,k) < n:
            return lo

# Input: no input
# Output: a string denoting all test cases have passed
#def test_cases():
  # write your own test cases

  #return "all test cases passed"

def main():
  in_file = open("work.in", "r")
  num_cases = int((in_file.readline()).strip())

  for i in range(num_cases):
    inp = (in_file.readline()).split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

if __name__ == "__main__":
  main()
