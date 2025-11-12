def insertion(a):
    for i in range(len(a)):
        for j in range(i, 0, -1):
            if a[j] < a[j-1] and j > 0:
                temp = a[j]
                a[j] = a[j-1]
                a[j-1] =a[j]

l = [6, 5, 4, 3, 2,1 ]
insertion(l)
print(l)

