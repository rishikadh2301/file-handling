import random
import time
"""
This script will sort a random array through insertion and merge sort techniques,
can find a value from the array using linear and binray search methods.
It also can handle large data structures and sort them using merge sort and aslo search for specific values from the large data.

"""

def generate_sorted_data(small_data, size): 
    '''
    This function sorts the random list linearly 
    generate_sorted_data1(size)
    size : number of elements in the list

    '''
    for j in range(size-1):
        for i in range(size-1):
            if small_data[i]>small_data[i+1]:
                small_data[i],small_data[i+1]=small_data[i+1],small_data[i]

            elif small_data[i]<small_data[i+1]:
                pass
                
            else:
                pass
    return small_data
    
def binary_search(sorted_array, target, start, end):
    '''
    This function finds an element in a sorted list which uses the technique divide and conquer
    binary_search(sorted_array, target, start, end)

    sorted_array : a sorted array returned from a sort function
    target : element which is to be found
    start : starting element
    end : ending element

    
    '''
    if start > end:
        return None
    else:
        mid = (start + end) // 2
        if target == sorted_array[mid]:
            return mid
        elif target > sorted_array[mid]:
            return binary_search(sorted_array, target, mid + 1, end) # start is mid + 1
        else:
            return binary_search(sorted_array, target, start, mid-1) # end is mid - 1
        


def generated_sorted_data1(arr):
    '''
    This function generates sorted array using merge sort
    generated_sorted_data(arr)
    arr: the  unsorted array that needs to be sorted

    '''
    if(len(arr)<=1): #if lenght of array is one then its already sorted 
        return arr
    mid=len(arr)//2  #divide the array into two and get the middle elememt
    left_arr=generated_sorted_data1(arr[:mid])  #recursion to divide the sub arrays again to be sorted
    right_arr=generated_sorted_data1(arr[mid:])
    
    sorted_arr=[]
    i=j=0
    while i <len(left_arr) and j< len(right_arr):
        if left_arr[i]<=right_arr[j]:
            sorted_arr.append(left_arr[i])
            i+=1
        else:
            sorted_arr.append(right_arr[j])
            j+=1
    sorted_arr+=left_arr[i:]
    sorted_arr+=right_arr[j:]
    return sorted_arr
 

def linear_search(array, value):
    '''
    This function uses linear search to search and return the index of a target value
    linear_search(my_array, value)
    my_array : the array in which we are looking for the target value
    value : the element which needs to be found

    
    '''
    for index in range(len(array)):
        if value == array[index]:
            return index
    return -1

def time_counter():
    '''
    This function finds the amount of time linear search and binary search take to find the same target
    compares time complexity of linear and binary search to see which is better
    time_counter()

    '''
    large_data = [55, 22, 89, 34, 67, 90, 15, 72, 39, 44]+[random.randint(1, 100) for _ in range(1000)]
    sorted_data = generated_sorted_data1(large_data)

    target = 72
    l_total=0
    b_total=0

    # linear search
    l_start = time.perf_counter() 
    l_result = linear_search(large_data, target) 
    l_end = time.perf_counter()
    l_total+= (l_end - l_start)
    l_average = l_total *1000000
    
    # binary search
    b_start = time.perf_counter()
    b_result = binary_search(sorted_data, target, 0, len(sorted_data) - 1) 
    b_end = time.perf_counter() 
    b_total += (b_end - b_start)
    b_average = b_total *1000000
    print(f"Linear search target position: {l_result}   time taken:{l_average} seconds")
    print(f"Binary search target position: {b_result}   time taken:{b_average} seconds")



def main():
    '''
    This is the main function to call all the other functions
    main()

    '''

    large_data = [55, 22, 89, 34, 67, 90, 15, 72, 39, 44] + [random.randint(1, 100) for _ in range(990)]
    small_data = [34, 7, 23, 32, 5, 62, 29, 12, 40, 8]
    obj=generate_sorted_data(small_data,len(small_data))
    obj2=generated_sorted_data1()
    print(obj)

    time_counter()
    

if __name__=="__main__":
    main()
