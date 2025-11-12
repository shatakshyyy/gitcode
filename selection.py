def sort(nums):
    for i in range(5):
        minpos = i
        for j in range(i, 6):
            if nums[minpos]> nums[j]:
               minpos = j


        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
        print(nums)

nums = [7, 3, 8, 4, 5, 9]
sort(nums)
print(nums)
         
