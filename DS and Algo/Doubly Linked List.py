class Node:
    def __init__(self,value=None):
        self.value= value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail= None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node= node.next

    # Creation of DLL
    def createDLL(self,nodeValue):
        node = Node(nodeValue)
        node.next=None
        node.prev= None
        self.head=node
        self.tail = node
        return "The creation of DLL is successful"
    # Insertion in DLL
    def InsertDLL(self,nodeValue,location):
        if self.head is None:
            return "No node found in DLL"
        else:
            newNode= Node(nodeValue)
            if location ==0: # If entered first place
                newNode.prev = None
                newNode.next = self.head
                self.head.prev =newNode
                self.head=newNode
            elif location ==1: # entry in last place
                newNode.next = None
                newNode.prev =self.tail
                self.tail.next =newNode
                self.tail=newNode
            else: ############ Any specific location
                tempNode = self.head
                index = 0
                while index< location-1:
                    tempNode = tempNode.next
                    index +=1
                newNode.next =tempNode.next
                newNode.prev =tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
            return "Node has been successgully inserted"

    # Traversing in DLL
    def traverse(self):
        if self.head is None:
            return "No Node to traverse"
        else:
            tempNode = self.head
            while tempNode is not None:
                print(tempNode.value)
                tempNode=tempNode.next

    # reverse Traverse a DLL
    def reversetraverse(self):
        if self.head== None:
            return "No node to traverse"
        else:
            tempNode =self.tail
            while tempNode is not None:
                print(tempNode.value)
                tempNode =tempNode.prev

    # Searching for a node
    def search(self,nodeValue):
        if self.head==None:
            return "The is nothing in DLL to search"
        else:
            tempNode = self.head
            while tempNode is not None:
                if tempNode.value == nodeValue:
                    print(f"Node {tempNode.value} Found")
                tempNode = tempNode.next
            return "Node you're searching does not exist in DLL"

    # Delete a node from DLL
    def deleteNode(self,location):
        if self.head is None:
            return "No Node exist to delete"
        else:
            if location==0: # First Postion
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location==1: # Last position
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                tempNode= self.head
                index=0
                while index<location-1:
                    tempNode = tempNode.next
                    index+=1
                tempNode.next =tempNode.next.next
                tempNode.next.prev = tempNode
            print("The Node has been successfully deleted")

    # Delete Everything from DLL
    def deleteDLL(self):
        if self.head is None:
            return "No Node exist in DLL"
        else:
            tempNode= self.head
            while tempNode is not None:
                tempNode.prev=None
                tempNode = tempNode.next
            self.head=None
            self.tail=None
        print("The Doubly Linked List has been completely deleted")

    def reverseDLL(self):
        if self.head is None:
            print("Nothing to reverse")
        else:
            currNode = self.head
            while currNode:
                nextNode = currNode.next
                currNode.next= currNode.prev
                currNode.prev = nextNode
                if currNode.prev == None:
                    break
                currNode=currNode.prev
        return currNode

doublyLL= DoublyLinkedList()
doublyLL.createDLL(1)
doublyLL.InsertDLL(2,1)
doublyLL.InsertDLL(3,1)
doublyLL.InsertDLL(4,1)
doublyLL.InsertDLL(5,1)
doublyLL.InsertDLL(10,4)

print([node.value for node in doublyLL])
doublyLL.reverseDLL()
print([node.value for node in doublyLL])

