# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
def merge_tuples (tuples_list):
    tuples_list.sort()
    #new_list =
    new_list = []
    split_one = []
    split_two = []
    split_three = []
    split_four = []
    temp_list = []
    low_int = tuples_list[0]
    
    for i in range(len(tuples_list)):
  
        if range(tuples_list[i][1]) == range(tuples_list[0][1]):
            if tuples_list[i][1] > tuples_list[0][1]:
                split_two.append(tuples_list[i])
                #print("high")
            else: 
                split_one.append(tuples_list[i])
                #print('low')
        elif  range(tuples_list[i][1]) != range(tuples_list[0][1]):
            temp_list.append(tuples_list[i])

    for i in range(len(temp_list)):
        
        if range(temp_list[i][1]) != range(tuples_list[i+1][1]) and i != len(temp_list) -1:
            
            #new_list.append(tuples_list[i+1])
            if temp_list[i-1][1] < temp_list[i+1][1] and temp_list[i][1] < temp_list[i+1][1] and temp_list[i-1][1] < temp_list[i][1]\
            and range(temp_list[i][1]) != range(temp_list[2][1]):
                if range(temp_list[i-1][1]) != range(temp_list[i+1][1]) :
            
                    new_list.append((temp_list[i][0],temp_list[i+1][1]))
             
            elif temp_list[i-1][1] > temp_list[i+1][1]:
                split_four.append(temp_list[i])
    

    if (max(split_one)[1]) > split_one[0][1] :
        new_list.append((split_one[0][0],(max(split_one)[1])))
    else:
        
        new_list.append(split_one[0])
   
    if (max(split_two)[1]) > split_two[0][1] :
        new_list.append((split_two[0][0],(max(split_two)[1])))


    
            
            

        
   
    new_list.sort() 
    return new_list
 
        
    
    
    

# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval

def sort_by_interval_size (tuples_list):
    lst_size = []
    k = 0
    i = 0
    j = 0
    m = 0
    final_list = ['' ,'' ,'' ,'' ,'' ]
    #print(tuples_list)
    while i < len(tuples_list):
        k = tuples_list[i][1]-tuples_list[i][0]
        lst_size.append(k)
        i = i+1
    lst_size.sort()
    
    while j < len(tuples_list):
        lst_coord = tuples_list[j][1] - tuples_list[j][0]
        perf_coord = lst_size.index(lst_coord)
        #print(perf_coord)
        
        final_list[lst_size.index(lst_coord)] = tuples_list[j]
        
        j = j+1
    return final_list


    
    
    

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
    assert merge_tuples([(1,2)]) == [(1,2)]
  # write your own test cases
    assert sort_by_interval_size([(1,3), (4,5)]) == [(4,5), (1,3)]
  # write your own test cases

    return "all test cases passed"

def main():
    intervals_in = open('intervals_in.in', 'r')

    intervals_amount = int(intervals_in.readline())
    tuples_list = []
    
    for _ in range(intervals_amount):
        interval_line = intervals_in.readline().strip().split()
        low_end = int(interval_line[0])
        high_end = int(interval_line[1])
        tupe_interval = low_end, high_end
        tuples_list.append(tupe_interval)

    
  

    print(merge_tuples(tuples_list))
  # open file intervals.in and read the data and create a list of tuples
    print(sort_by_interval_size (merge_tuples(tuples_list)))
  # merge the list of tuples

  # sort the list of tuples according to the size of the interval

  # run your test cases
  
  #print (test_cases())
  

  # open file intervals.out and write the output list of tuples
  # from the two functions

if __name__ == "__main__":
    main()
