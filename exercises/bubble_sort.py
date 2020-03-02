
def sortBubble(nums):
    for x in range(len(nums)-1, 0, -1):
        for y in range(x):
            if nums[y]>nums[y+1]:
                t = nums[y]
                nums[y] = nums[y+1]
                nums[y+1] = t


numbers = [5, 3, 8, 6, 7, 2]
sortBubble(numbers)

print (numbers)