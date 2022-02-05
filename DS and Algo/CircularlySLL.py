class Node:
    def __init__(self,value= None):
        self.value = value
        self.next = None
class CircularSibglyLinkedList:
    def __init__(self):
        self.head= None
        self.tail= None
    def __iter__(self):
        node= self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node=node.next

    # Creation of CircularSLL
    def CircularSLL(self,nodeValue):
        node= Node(nodeValue)
        node.next= node
        self.head= node
        self.tail= node
        return "CSLL is successfully created"

    # Insertion of nodes
    def insertCSLL(self,value,location):
        if self.head is None:
            return "There is no node to insert into"
        else:
            newNode= Node(value)
            if location == 0: # at beginning
                newNode.next = self.head # new node's reference value is linked to head
                self.head= newNode # it will create a link between head and node
                self.tail.next = newNode # tail's reference value =  newNode's physical location
            elif location == 1: # Insertion at last
                newNode.next= self.tail.next
                self.tail.next= newNode
                self.tail=newNode
            else:
                tempNode= self.head
                index=0
                while index < location - 1:
                    tempNode= tempNode.next
                    index+=1
                nextNode= tempNode.next
                tempNode.next= newNode
                newNode.next= nextNode
            return "Node had been succesfully inserted!!"

    # Traversing through CSLL
    def traverse(self):
        if self.head is None:
            print("Nothing to traverse")
        else:
            tempNode= self.head
            while tempNode is not None:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:  # To Check if we have reached the last node
                    break
    # SEarching in the CSLL
    def searchCSLL(self,nodeValue):
        if self.head is None:
            return "Nothing to search"
        else:
            tempNode= self.head
            while tempNode is not None:
                if tempNode.value==nodeValue:
                    print(tempNode.value)
                tempNode= tempNode.next
                # the loop will be infinitely long. to stop that we have to give a condition
                if tempNode== self.tail.next:
                    return "The node doesn't exist in this CSLL"
# We can also print whether it exist or not along with the index position of the node
# To learn how, see SLL example of search

    # Deletion
    def deleteCSLL(self,location): # O(n) - Time complexity and O(1) Space Complexity
        if self.head is None:
            print("There is no node in CSLL")
        else:
            if location ==0: # At the beginning
                if self.head== self.tail: # If there is only 1 node
                    self.head.next= None
                    self.tail=None
                    self.head=None
                else:
                    self.head = self.head.next
                    self.tail.next=self.head
            elif location==1: # last position
                if self.head== self.tail: # If there is only 1 node
                    self.head.next= None
                    self.tail=None
                    self.head=None
                else: ########### For Multiple Nodes #############
                    node= self.head
                    while node is not None: # LOOP
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next= self.head
                    self.tail= node
            else:
                tempNode= self.head
                index= 0
                while index < location -1:
                    tempNode = tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    # Delete entire CSLL
    def deletefullCSLL(self):
        self.head= None
        self.tail.next= None
        self.tail=None

circularSLL= CircularSibglyLinkedList()
print(circularSLL.CircularSLL(1))
circularSLL.insertCSLL(0,0)
circularSLL.insertCSLL(2,1)
print([node.value for node in circularSLL])

circularSLL.deletefullCSLL()
print([node.value for node in circularSLL])




