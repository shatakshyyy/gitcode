def ins(a):
    for i in range(len(a) -1):
        k = i
        j = i+1
        while j > 0:
            if a[j] < a[k]:
                (a[j], a[k]) = (a[k], a[j])
            k = k - 1
            j = j -1
            

a = [4, 5, 34, 8, 0, 6, 7]
print(a)
ins(a)
print(a)