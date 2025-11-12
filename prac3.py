def quick(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    left = [ x for x in a[1:] if x <pivot]
    right = [x for x in a[1:] if x>= pivot]

    return quick(left) + [pivot] + quick(right)


a =[6, 4 ,6, 5, 3 ,2, 0]

print(f"the unsorted list {a}")
print("sorted lizt", quick(a))