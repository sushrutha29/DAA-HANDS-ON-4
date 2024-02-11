"""Given K sorted arrays of size N each, the task is to merge them all maintaining their sorted order.

Examples: 

Input: K = 3, N =  4
array1 = [1,3,5,7]
array2 = [2,4,6,8]
array3 = [0,9,10,11]
Output: [0,1,2,3,4,5,6,7,8,9,10,11]
Merged array in a sorted order where every element is greater than the previous element.

"""

import heapq

def mergesort(arr):
    finalresult = []
    heap = []

    for i, array in enumerate(arr):
        if array:  
            heapq.heappush(heap, (array[0], i, 0)) 

    while heap:
        value, array_index, index_within_array = heapq.heappop(heap)
        finalresult.append(value)

        index_within_array += 1

        if index_within_array < len(arr[array_index]):
            heapq.heappush(heap, (arr[array_index][index_within_array], array_index, index_within_array))

    return finalresult

# Example usage:
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
arr3 = [0, 9, 10, 11]

finalresult = mergesort([arr1, arr2, arr3])
print(finalresult)
