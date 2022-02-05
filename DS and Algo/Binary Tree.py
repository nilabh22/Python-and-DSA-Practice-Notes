# We will discuss the Binary Tree the different operations we can perform on it.
# Main is Traversal which includes -
# 1. PreOrder Traversal
# 2. InOrder Traversal
# 3. PostOrder Traversal
# 4. LevelOrder Traversal
import Queue as queue

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild =rightChild



def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
#preOrderTraversal(newBT)

def inOrderTraversal(rootnode):
    if not rootnode:
        return
    inOrderTraversal(rootnode.leftChild)
    print(rootnode.data)
    inOrderTraversal(rootnode.rightChild)

#inOrderTraversal(newBT)

def postOrderTraversal(rootnode):
    if not rootnode:
        return
    postOrderTraversal(rootnode.leftChild)
    postOrderTraversal(rootnode.rightChild)
    print(rootnode.data)

#postOrderTraversal(newBT)

def levelOrderTraversal(rootnode): # It works with queue data structures
    if not rootnode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootnode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

#levelOrderTraversal(newBT)
##### We ar using "LEVEL ORDER TRAVERSAL" to search the node in a tree
def searchBT(rootnode, nodevalue):
    if not rootnode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootnode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodevalue:
                return "Success"
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return "Not Found"

#print(searchBT(newBT,"Coffee"))

def insertNodeBT(rootnode, newNode):
    if not rootnode:
        rootnode = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootnode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Success"

            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Success"

#newNode = TreeNode("Cola")
#print(insertNodeBT(newBT,newNode))
#print(levelOrderTraversal(newBT))


################## DELETE A NODE FROM BINARY TREE ######################

def getDeepestNode(rootnode):
    if not rootnode:
        return "No BT exists"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootnode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        deepestnode = root.value
        return deepestnode

#deepestNode = getDeepestNode(newBT)
#print(deepestNode.data)

def deleteDeepestNode(rootnode,dNode):
    if not rootnode:
        return "BT doesn't exists"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootnode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value == dNode:
                root.value =None
                return
            if root.value.rightChild:
                if root.value.rightChild == dNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild == dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)

#newNode = getDeepestNode(newBT)
#deleteDeepestNode(newBT,newNode)
#levelOrderTraversal(newBT)

def deleteNode(rootnode, node):
    if not rootnode:
        return "No Binary tree Exists"
    else:
        customQueue =queue.Queue()
        customQueue.enqueue(rootnode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootnode)
                root.value.data = dNode.data
                deleteDeepestNode(rootnode,dNode)
                return "The node has been deleted from BT successfully"
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue((root.value.rightChild))
        return "Failed to Delete"
##########3 The "Hot" node will be deleted and the deepest node will take its place
#deleteNode(newBT,"Hot")
#levelOrderTraversal(newBT)

def deleteBT(rootnode):
    rootnode.data = None
    rootnode.leftChild =None
    rootnode.rightChild =None

    return "The BT has been deleted"

#print(deleteBT(newBT))
#levelOrderTraversal(newBT)