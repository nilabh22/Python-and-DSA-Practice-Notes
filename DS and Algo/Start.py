# Recursion - Solving a problem with the help of same problem
# We ccan us recursion when we know we can break the problem into simpler subproblems of the same typr
def russiandoll(doll):
    if doll <1:
        print("All dolls are opened")
    else:
        russiandoll(doll-1)
        print(doll)
russiandoll(3)

## Example of writing recursion in 3 steps
# Printing factorial of a number
def factorial(n):
    assert n >=0 and int(n) == n,'Enter a positive integer only !!'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1) # We break our problem of n! = n* (n-1)!
print(factorial(9))

## Example of writing fabonacci series
# Fabonacci series is the series of numbers where the number is the sum of its 2 preceding numbers
# 0,1,1,2,3,5,8,13.....

# Interview Questions
def fabonacci(n):
    assert n>=0 and int(n)==n,"Fibonacci number cannot be nagative or non integer!"
    if n in [0,1]:
        return n
    else:
        return fabonacci(n-1) + fabonacci(n-2)


print(fabonacci(7))

# Interview questions asked related to recursion
#Question 1 - Sum of digits using recursion
def sumofdigits(n):
    assert n>=0 and int(n) ==n,'Enter positive interger'
    if n in [0]:
        return 0
    else:
        return int(n%10) + sumofdigits(int(n/10))
print(sumofdigits(98))

#Question 2 - Power of a number using recursion
def powerofnum(x,n):
    assert x>=0 and n>=0 and x==int(x) and n==int(n),'Values should be positive'
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x * powerofnum(x,n-1)

print(powerofnum(9,4))


# Example 3 - GCD of two numbers

def gcd(a,b):
    assert int(a)==a and int(b)==b, 'Values must be integers'
    if a <0:
        a = -1 * a
    if b<0:
        b= -1 * b
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

print(gcd(-48,18))

# Example 4 - Decimal to binary using recursion
def dectobin(n):
    assert int(n)==n,'Enter positive number'
    if n ==0:
        return 0
    else:
        return n%2 + 10 * dectobin(int(n/2))
print(dectobin(2))


# It will ask user to enter the no. of days for which user wants temperature data
def avgtem():
    temp = int(input("How many days average temperature you want: "))
    sum = 0
    templist = []
    for i in range(1, temp + 1):
        daytemp = int(input("Enter Day" + str(i) + "'s temperature: "))
        templist.append(daytemp)
        sum += daytemp
    avg = sum / temp
    print(avg)

    avgcount = 0
    for j in templist:
        if j > avg:
            avgcount += 1
    print(str(avgcount) + " days temperture are above average temperature")

avgtem()

#Kadane's ALGORITHM
def maxSubArray(self, nums: List[int]) -> int:
    currSum = 0
    maxSoFar = nums[0]
    start, end, poi = 0, 0, 0

    for i in range(0, len(nums)):
        currSum += nums[i]
        if (maxSoFar < currSum):
            maxSoFar = currSum
            start, end = poi, i

        if (currSum < 0):
            currSum = 0
            poi = i + 1

    return maxSoFar

def maxSubArray(self, nums: List[int]) -> int:
    currMax = globalMax = nums[0]
    for i in range(1, len(nums)):
        currMax = max(nums[i], currMax + nums[i])
        if currMax > globalMax:
            globalMax = currMax
    return globalMax
