def bubble(a):
    for i in range(n-1):
        for j in range(n - 1 - i):
            if a[j+1] < a[j]:
                temp = a[j]
                a[j] = a[ j+1]
                a[j+1] = temp


list = []
n = int(input("enter the value"))

for i in range(n):
    x = int(input("enter the element of list"))
    list.append(x)

print("the unsorted list", list)

bubble(list)
print("the sorted list", list)