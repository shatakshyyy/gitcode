def bub(a):
    for i in range(len(a)-1):
        for j in range(0, len(a)-1 - i):
            if a[j] > a[j+1]:
                (a[j], a[j+1]) = (a[j+1], a[j])

a =[ 4, 5, 3, 6, 7, 1, 8, 2]

print(a) 
bub(a)
print(a)

def sel(a):
    for i in range(len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[j] < a[min]:
                min = j

        (a[min], a[i]) = (a[i], a[min])

a = [3, 2, 6, 5, 8, 1 ]

print(a)
sel(a)
print(a)
