# Binary heap is same as that of binary tree, carrying the same properties of it.
# It is faster implementation than array or linked list as it provides solution in O(logN) time.
# Example - if u want to insert a number in a set of numbers, array will take O(n) in worst case, and same for the Linked list,as
# we wll have to traverse through the linked list to find the appropriate position.


################ Properties of Binary Heap ##################
# The rootnode's value will be either less than the value of its child or greater than them.
# Min Heap will have a rootnode whose value is less than their childs
# Max heap is vice versa of min heap

######## PRACTICAL USE #########
# 1. Prim's Algorithm
# 2. Heap Sort
# 3. Priority Queue

class Heap:
    def __init__(self,size): #O(1)
        self.customList = (size+1) * [None]
        self.maxSize = (size + 1)
        self.heapSize = 0

def peek(rootNode): #O(1) #PEEK = ROOTNODE
    if not rootNode:
        return
    return rootNode.customList[1]

def sizeofHeap(rootNode): #O(1)
    if not rootNode:
        return
    else:
        return rootNode.heapSize

def levelOrderTraversal(rootNode): #O(n)
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapSize+1):
            print(rootNode.customList[i])

def heapifyTreeInsert(rootNode, index , heapType): # O(LogN) - space and time
    # this function is made to maintain the binary heap tree orientation.
    # when value is inserted into binary heap it swaps it to mix or max accordingly.

    parentIndex = int(index/2)
    if index <=1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]: # means we swap the nodes
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)

    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode,parentIndex,heapType)

def insertHeap(rootNode, nodeValue, heapType): # O(logN) - space and time
    if rootNode.heapSize + 1 == rootNode.maxSize: # +1 because we are already starting from 0
        return "The Binary Heap is Full"
    rootNode.customList[rootNode.heapSize +1] = nodeValue
    rootNode.heapSize +=1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return f"The {0} had been inserted in Binary heap".format(nodeValue)

def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index*2
    rightIndex = index*2 + 1
    swapChild =0

    if rootNode.heapSize < leftIndex:
        return
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftindex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftindex]
                rootNode.customList[leftindex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftindex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftindex]
                rootNode.customList[leftindex] = temp
            return
    else:
        if heapType =="Min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[leftindex]
                rootNode.customList[leftindex] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
    heapifyTreeExtract(rootNode,swapChild,heapType)

def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] =rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -=1
        heapifyTreeExtract(rootNode,1,heapType)
        return extractedNode

def entireBinaryHeap(rootNode):
    rootNode.customList =None


newBinaryHeap = Heap(5)
insertHeap(newBinaryHeap, 4, "Max")
insertHeap(newBinaryHeap, 5, "Max")
insertHeap(newBinaryHeap, 2, "Max")
insertHeap(newBinaryHeap, 1, "Max")
entireBinaryHeap(newBinaryHeap)
levelOrderTraversal(newBinaryHeap)