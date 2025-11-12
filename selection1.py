# in selection sort we select the minimum element and compare it with other and update the value i f
#we find min, at the end of each pass we update the value of min by swapping it to the minimum value


def selection(array):
    for i in range(n-1):
        minindex = i
        for j in range(i, n):
            if array[minindex] > array[j]:
                
                minindex = j

        temp = array[i]
        array[i] = array[minindex]
        array[minindex]  = temp


n= int(input("enter the value"))
list = []
for i in range(n):
    x = int(input("list element"))
    list.append(x)

print("the unsorted list", list)
selection(list)
print("the sorted list", list)
        

