import time
from itertools import permutations

def quick(a):
    if len(a) <= 1:
        return a
    
    else:
        piv = a[0]
        left = [x for x in a[1:] if x < piv]
        right = [ x for x in a[1:] if x >= piv]
        return quick(left) + [piv] + quick(right)
    

a = [5, 7, 3, 8, 6, 4]

print("the unsorted list", a)
l = []

for p in permutations(a):
    st = time.time()
    quick(a)
    et = time.time()
    t_time = et - st
   
    l.append(t_time)

average = float(sum(l)/len(l))


print("best case complexity", min(l))
print("worst case complexity", max(l))
print("average case complexity", average)


