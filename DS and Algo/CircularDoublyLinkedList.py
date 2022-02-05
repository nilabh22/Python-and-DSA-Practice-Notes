from random import randint

class Node:
    def __init__(self,value=None):
        self.value= value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail= None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node= node.next
            if node ==self.tail.next:
                break

    # Creation of CDLL
    def createCDLL(self,nodevalue):
        newNode = Node(nodevalue)
        self.head= newNode
        self.tail= newNode
        newNode.prev = newNode
        newNode.next = newNode
        return "The new CDLL has been created"

    # Insertion in CDLL
    def insertCDLL(self,nodeValue,location):
        if self.head is None:
            return "No Nodes found in CDLL"
        else:
            newNode = Node(nodeValue)
            if location==0: # At the beginning
                newNode.prev = self.tail
                newNode.next =self.head
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location==1: # At the last
                newNode.next= self.head
                newNode.prev=self.tail
                self.head.prev=newNode
                self.tail.next =newNode
                self.tail=newNode
            else:
                currNode = self.head
                index =0
                while index < location-1:
                    currNode=currNode.next
                    index+=1
                newNode.next=currNode.next
                newNode.prev=currNode
                newNode.next.prev =newNode
                currNode.next =newNode
            return "Node has been successgully inserted"

    # Traversing in CDLL
    def traverse(self):
        if self.head is None:
            return "Nothing to traverse"
        else:
            tempNode=self.head
            while tempNode is not None:
                print(tempNode.value)
                tempNode=tempNode.next
                if tempNode==self.tail.next:
                    break

    # reverse Traverse a CDLL
    def reversetraverse(self):
        if self.head== None:
            return "No node to traverse"
        else:
            tempNode =self.tail
            while tempNode:
                print(tempNode.value)
                tempNode =tempNode.prev
                if tempNode==self.head.prev:
                    break

    # Searching a node in CDLL
    def searchCDLL(self,nodeValue):
        if self.head==None:
            return "Nothing to search in CDLL"
        else:
            tempNode= self.head
            while tempNode != None:
                if tempNode.value==nodeValue:
                    return tempNode.value
                if tempNode.value == self.tail.next:
                    print("Node not exist in CDLL")
                tempNode=tempNode.next

    # Deletion of CDLL in CDLL
    def deleteNode(self,location):
        if self.head is None:
            return "No node exist in CDLL"
        else:
            if location ==0:
                if self.head==self.tail:
                    self.head.prev= None
                    self.head.next= None
                    self.tail=None
                    self.head=None
                else:
                    self.head=self.head.next
                    self.head.prev=self.tail
                    self.tail.next = self.head
            elif location==1:
                if self.head==self.tail:
                    self.head.prev= None
                    self.head.next= None
                    self.tail=None
                    self.head=None
                else:
                    self.tail=self.tail.prev
                    self.tail.next= self.head
                    self.head.prev =self.tail
            else:
                curNode=self.head
                index=0
                while index<location-1:
                    curNode=curNode.next
                    index+=1
                curNode.next=curNode.next.next
                curNode.next.prev=curNode

    # Delete Everything from DLL
    def deleteCDLL(self):
        if self.head is None:
            return "No Node exist in DLL"
        else:
            self.tail.next=None
            tempNode= self.head
            while tempNode is not None:
                tempNode.prev=None
                tempNode = tempNode.next
            self.head=None
            self.tail=None
        print("The Doubly Linked List has been completely deleted")


CircularlyDSLL = CircularDoublyLinkedList()
CircularlyDSLL.createCDLL(1)
CircularlyDSLL.insertCDLL(0,0)
CircularlyDSLL.insertCDLL(2,1)
CircularlyDSLL.insertCDLL(3,1)
CircularlyDSLL.insertCDLL(4,1)
CircularlyDSLL.insertCDLL(10,3)


print([node.value for node in CircularlyDSLL])
