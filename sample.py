def quick(a, lb, up):
    piv = a[0]
    while(lb<up):
        while(a[lb] <= piv):
            lb +1

        while(a[up] > piv):
            up - 1

        (a[lb], a[up]) = (a[up], a[lb])

    (piv, a[up]) = (a[up], piv)

    quick(a, lb, piv-1)
    quick(a, piv, up)

    
         

        
list = []

n = int(input("enter the value"))

for i in range(n):
    x = int(input("enter the element of list"))
    list.append(x)

print("the unsorted list", list)

quick(list, 0, n)
print("the sorted list", list)