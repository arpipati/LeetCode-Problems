## Problem URL: https://leetcode.com/problems/duplicate-zeros/

'''
Algorithm:

Part One:
- For any array, we first need to find the total number of zeros that need to be duplicated.

- We have an Edge Case when there is a zero which cannot be duplicated, as it would exceed the array size.

- To find this edge case, we check for the last element in the array which will not be deleted. 

- We find this by subtracting number of zeros from the length of the array

Part Two:
- Once we know the number of zeros and the position of the last element that should be included in the new array, 

- We iterate over the array in descending order staring from the position of last element. 

- If we encounter a "0", we copy that element twice.

- else, we copy it one time.

'''

arr = [1,0,2,3,0,4,5,0]
print("Original Array:", arr)
zero_count = 0

arrLen = len(arr) - 1

for z in range(arrLen):
    if arr[z] == 0:
        ## Edge Case, when the element at zth position is 0. However, if zth postion is the last position in the array before it is copied, we just copy 0 directly at the end only once.
        if z == arrLen - zero_count:
            arr[arrLen] = 0
            arrLen -= 1
            break
        zero_count += 1

## Now that we know the number of zeroes and the position on the last element that should be in the new array (arrLen - zero_count), we can iterate backwards.

last = arrLen - zero_count

for i in reversed(range(last)):
    if arr[i] == 0:
        arr[i + zero_count] = 0
        zero_count -= 1
        arr[i + zero_count] = 0

    else:
        arr[i + zero_count] = arr[i]

print("New Array:", arr)