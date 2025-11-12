#divide and conquer algorithm
import time
from itertools import permutations
def merge(nums):
    if len(nums) > 1:
        left = nums[:len(nums)//2]
        right = nums[len(nums)//2:]

        merge(left)
        merge(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
                
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
        
list = [3, 6, 2,4 ,45 ,46 ,645 ]
print("the unsorted list", list)
l = []
for p in permutations(list):
    st = time.time()
    merge(list)
    et = time.time()
    t_time = et - st
   
    l.append(t_time)

print("best time complexity", min(l))
print("worst time complexity", max(l))
print("average time complexity", sum(l)/ len(l))