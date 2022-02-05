####################### SORTING ########################

# 1. Bubble Sort - Only to use when we need less space. ALso, it is easy to implement.
# Time Complexity - O(N^2) ans space complexity is O(1).
import math


def bubbleSort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1): # -i-1 bcoz we have to compare to a value less to i.
            if list[j] > list[j+1]:
                list[j], list[j+1]= list[j+1], list[j]
    print(list)

# 1. Poor Time Complexity in best case
# 2. Best for short random digits, not suited for the list in descending order.
# 3. Space friendly

def selectionSort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i+1, len(list)):
            if list[min_index] > list[j]:
                min_index =j
        list[i], list[min_index] = list[min_index], list[i]
    print(list)


# 1. Use insertion sort when space is issue.
# 2. when we have inflow of numbers & we want to keep them sorted

def insertionSort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j>=0 and key < list[j]:
            list[j+1] = list[j]
            j-=1
        list[j+1] = key
    print(list)

# Time complexity - O(n^2) (insertionSort is used) O(logN when quick sort is used in the place of insertion sort)
# Space Complexity - O(N)
def bucketSort(customList):
    numberofBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    for i in range(numberofBuckets):
        arr.append([])
    for j in customList:
        index_b = math.ceil(j * numberofBuckets / maxValue)
        arr[index_b - 1].append(j)

    for i in range(numberofBuckets):
        arr[i] = insertionSort(arr[i])

    k = 0
    for i in range(numberofBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList


def merge(customList, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = customList[l + i]

    for j in range(0, n2):
        R[j] = customList[m + 1 + j]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1

def mergeSort(customList, l, r): # Time - O(NlogN) and Space - O(N)
    if l < r:
        m = (l + (r - 1)) // 2
        mergeSort(customList, l, m)
        mergeSort(customList, m + 1, r)
        merge(customList, l, m, r)
    return customList


def partition(customList, low, high):
    i = low - 1
    pivot = customList[high]
    for j in range(low, high):
        if customList[j] <= pivot:
            i += 1
            customList[i], customList[j] = customList[j], customList[i]
    customList[i + 1], customList[high] = customList[high], customList[i + 1]
    return (i + 1)


def quickSort(customList, low, high):
    if low < high:
        pi = partition(customList, low, high)
        quickSort(customList, low, pi - 1)
        quickSort(customList, pi + 1, high)


def heapify(customList, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and customList[l] < customList[smallest]:
        smallest = l

    if r < n and customList[r] < customList[smallest]:
        smallest = r

    if smallest != i:
        customList[i], customList[smallest] = customList[smallest], customList[i]
        heapify(customList, n, smallest)


def heapSort(customList):
    n = len(customList)
    for i in range(int(n / 2) - 1, -1, -1):
        heapify(customList, n, i)

    for i in range(n - 1, 0, -1):
        customList[i], customList[0] = customList[0], customList[i]
        heapify(customList, i, 0)
    # customList.reverse()



cList = [2,1,7,6,5,3,4,9,8]
print(mergeSort(cList,0,8))
