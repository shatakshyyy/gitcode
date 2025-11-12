def partition(a, lb, up):
    
    piv = a[lb]
    for i in range(lb, up):
        while(a[lb] <= piv):
            lb +1

        while(a[up] > piv):
            up - 1

        (a[lb], a[up]) = (a[up], a[lb])

    (piv, a[up]) = (a[up], piv)

    return a.index[piv]

        
         
def quick(a, lb, up):
    if lb < up:
        piv = partition(a, lb, up)

        quick(a, lb, piv-1)
        quick(a, piv+1, up)


        
list = []

n = int(input("enter the value"))

for i in range(n):
    x = int(input("enter the element of list"))
    list.append(x)

print("the unsorted list", list)

quick(list, 0, n-1)
print("the sorted list", list)




