 # quick sort is also a divide and conquer algorithm
import time
from itertools import permutations
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)
 
# Example usage
list = [1, 7, 4, 1, 10, 9, -2]
print("the unsorted list", list)
l = []
for p in permutations(list):
    st = time.time()
    quicksort(list)
    et = time.time()
    t_time = et - st
   
    l.append(t_time)

print("best time complexity", min(l))
print("worst time complexity", max(l))
print("average time complexity", sum(l)/ len(l))