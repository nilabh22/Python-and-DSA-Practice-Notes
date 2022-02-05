############ Binary Search Tree ###############

# 1. Binary Search Tree is faster then Binary tree
# 2. The left child will always be less or equal to the parent node.
# 3. The right child child of the BST will always be greater than the parent node

import Queue as queue

class BSTNode:
    def __init__(self,data): # O(1) Time and space
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertBST(rootNode, nodeValue): # O(LogN) space and time because it took LogN time to insert in stack memory
    if rootNode.data == None: # If rootnode doesnot exists
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data: # for left child
        if rootNode.leftChild is None: # if leftnode is none in BST, we insert nodevalue in the leftChild of rootnode.
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertBST(rootNode.leftChild, nodeValue) # If leftnode already exists, we recursively add to the leftnode
    else:  ### SIMILARLY we do it for right node
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertBST(rootNode.rightChild, nodeValue)
    return "The node has been successfully Inserted"

################### TRAVERSING #######################

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

def searchBST(rootNode, nodeValue): # O(logN) space and time
    if rootNode.data == nodeValue: # edge case
        print("The nodeValue has been found")
    elif nodeValue < rootNode.data:
        if nodeValue == rootNode.leftChild.data:
            print("The nodeValue has been found")
        else:
            searchBST(rootNode.leftChild, nodeValue)
    else:
        if nodeValue == rootNode.rightChild.data:
            print("The nodeValue has been found")
        else:
            searchBST(rootNode.rightChild, nodeValue)

############### DELETION ###################

def minNodeValue(bstNode): # This will search the minimum node in the BST
    current = bstNode
    while (current.leftChild is not None):
        current = current.leftChild
    return current

def deleteNode(rootNode, nodeValue): # O(logN) space and time complexity
    if rootNode is None: # if no value in rootNode, we retue rootnode
        return rootNode
    elif nodeValue < rootNode.data: # if nodevalue is less than rootNode's value, we recursively call delete in leftchild (bcoz value less then rootnode will always be on leftchild). Property of binary tree.
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data: # similarly for right
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else: # if we have only one(1) child in rootnode, then we assign rightright to rootnode
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        temp = minNodeValue(rootNode.rightChild) # we are finding succesor, which is the minimum nodevalue in the right Subtree of rootnode.
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)

    return rootNode
    print("Node has been deleted successfully")

def deleteBST(rootNode): # O(1) space and time
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None


#newBST = BSTNode(None)
#print(insertBST(newBST, 70))
#print(insertBST(newBST, 50))
#print(insertBST(newBST, 90))
#print(insertBST(newBST, 30))
#print(insertBST(newBST, 60))
#print(insertBST(newBST, 80))
#print(insertBST(newBST, 100))
#print(insertBST(newBST, 20))
#print(insertBST(newBST, 40))
#deleteBST(newBST)
#levelOrderTraversal(newBST)