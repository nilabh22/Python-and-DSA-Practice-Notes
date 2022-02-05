# STACK - Stack is a data structure that stores the data in a Last-In/First-Out
# Real life examples of stacks are pile of plates placed over each other, books placed over each other and bangles in the hand of a women.

# LIFO method - The stacks works on the principle of LIFO method which means the data that was put in stack at last will be lifted off/taken first.
'''The best example of stack data structure is "BACK BUTTON" in a browser.'''
# The website that will be opened in the last will be taken first.

##### Operations that we can perform on stack-
# 1. Create Stack
# 2. push()
# 3. pop()
# 4. peek()
# 5. isfull()
# 6. isempty()
# 7. delete()

######## Creation of Stack using List without size limit ##########

class Stack:
    def __init__(self):
        self.list =[] # O(1) -  Time and Space Complexity

    def __str__(self):
        values = self.list.reverse()
        values =[str(x) for x in self.list]
        return '\n'.join(values)

    #isEmpty()
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self,value):
        self.list.append(value)
        return "The value has been successfully inserted"

    def pop(self):
        if self.isEmpty():
            return "NO data in the Stack"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return " NO data"
        else:
            return self.list[len(self.list)-1]

    def delete(self):
        self.list = None
        return "Stack has been deleted"



#customStack = Stack()
#customStack.push(1)
#customStack.push(2)
#customStack.push(3)
#customStack.push(4)
#customStack.delete()
#print(customStack.isEmpty())

######### Using limited size ###############

class StackLim:
    def __init__(self,Maxsize):
        self.Maxsize = Maxsize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list ==[]:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list)== self.Maxsize:
            return True
        else:
            return False

    def push(self,value):
        if self.isFull():
            print("NO additional space in Stack memory to insert")
        else:
            self.list.append((value))

    def pop(self):
        if self.isEmpty():
            print("No data")
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            print("No data")
        else:
            return self.list[(len(self.list)-1)]

    def delete(self):
        self.list=None

#### Stacks using Linked List

class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node= self.head
        while node:
            yield node
            node=node.next

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values =[str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.LinkedList.head is None:
            print("Empty Linked List")
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue

    def peek(self):
        if self.LinkedList.head is None:
            print("Empty Linked List")
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue

    def delete(self):
        self.LinkedList.head  = None
        print("Stack has been deleted")

LinkedStack = Stack()
LinkedStack.push(1)
LinkedStack.push(2)
LinkedStack.push(3)
LinkedStack.push(4)
print(LinkedStack)

LinkedStack.delete()
print(LinkedStack)
