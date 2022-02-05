########## In addition to push() and pop(), Create a Stack which return minimum element in it but all should be operated in O(1) Time complexity.
# TO run in O(1), it should be made using linked list

class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        string= str(self.value)
        if self.next:
            string += ',' + str(self.next)
        return string

class Stack:
    def __init__(self):
        self.top = None
        self.minNode = None

    def min(self):
        if not self.minNode:
            return None
        return self.minNode.value

    def push(self, item):
        if self.minNode is not None and (self.minNode.value < item): # check if value of minNode is less than item, if yes,
            self.minNode = Node(value= self.minNode.value , next= self.minNode) # let the value of minNode remains same, else
        else:
            self.minNode = Node(value= item, next = self.minNode) # set minNode's  value to item
        # ADD this node to the top of the stack
        self.top = Node(value=item, next = self.top)

    def pop(self):
        if self.top is None:
            return None
        else:
            self.minNode =  self.minNode.next
            item = self.top.value
            self.top = self.top.next
            return item

#customStack = Stack()
#customStack.push(6)
#print(customStack.min())
#customStack.push(5)
#print(customStack.min())
#customStack.push(3)
#print(customStack.min())
#customStack.push(12)
#print(customStack.min())
#print('---------------')
#print(customStack.pop())
#print(customStack.min())
#print(customStack.pop())
#print(customStack.min())

####### Question 2 - Stack of Plates ######
# Create a stack of limited capacity and when it gets full make a new stack but when pop() method is called , it acts as one

class PlateStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def __str__(self):
        return self.stacks

    def push(self, item):
        if len(self.stacks) >0 and len(self.stacks[-1]) < self.capacity: # checking if there are elements in the stack or not
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item]) # else if the the elements are not present then we add in stack

    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) ==0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            self.stacks[-1].pop()

    def pop_at(self, stackNumber):
        if len(self.stacks[stackNumber]) >0:
            return self.stacks[stackNumber].pop()
        else:
            return None


customstack = PlateStack(2)
customstack.push(1)
customstack.push(2)
customstack.push(3)
print(customstack.pop_at(1))
