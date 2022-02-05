######## Kadane's algorithm for maximum subarray sum problem ###############
# maximum subarray problem means we have to find all the possible subarray and then return the maximum possible sum of the subarray
# [1,2,3,-1,5] - Brute force work as we use 2 for loops, find all subarray and then add all and finally return the subarray with the largest sum
# We apply KADANE's algorithm
def maxSubArraySum(self, arr, size):
    ##Your code here
    b_sum = float('-inf') # set biggest sum to  - infinity
    sum = 0 # create a variable
    for i in arr:
        sum = max(i, sum + i)
        b_sum = max(b_sum, sum)
    return b_sum

# Check weather Strings are Rotations of each other or not

def areRotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''

    # Check if sizes of two strings are same
    if size1 != size2:
        return 0

    # Create a temp string with value str1.str1
    temp = string1 + string1
    if string2 in temp:
        return 1
    return 0


if areRotations('aacb', 'caab'):
    print("str are rotations")
else:
    print('No')

