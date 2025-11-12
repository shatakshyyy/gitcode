#we divide the array in sorted and unsorted array

import time
from itertools import permutations

''' def permutation(lst):
 
    
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
 
    l = [] 
    for i in range(len(lst)):
       m = lst[i]
 
       
       remLst = lst[:i] + lst[i+1:]
 
       
       for p in permutation(remLst):
           l.append([m] + p)
    return l '''


def insertion(array):
    for i in range(len(array)):
        for j in range(i, 0, -1):
            if array[j] < array [j-1] and j > 0:
                temp = array[j-1]
                array[j-1] = array[j]
                array[j] = temp

list = [5, 3, 3,2,11, 1, 6]
n = int(input("enter the value"))

for i in range(n):
    x = int(input("enter the element of list"))
    list.append(x)

print("the unsorted list", list)
l = []
for p in permutations(list):
    st = time.time()
    insertion(list)
    et = time.time()
    t_time = et - st
   
    l.append(t_time)

print("best time complexity", min(l))
print("worst time complexity", max(l))
print("average time complexity", sum(l)/ len(l))
