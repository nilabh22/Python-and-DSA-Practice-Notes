from LinkedList import LinkedList
################ Removing Duplicates from a Linked List ###################
# 2 appraoches -  #1- using set() to automatically remove and then without set() method

def removeDuplicates(head):
    currNode = head # create a tempNode and set it to head value
    while currNode.next: # create a loop
        if currNode.value == currNode.next.value: # Compare the current Node's value to the next node's value
            currNode.next = currNode.next.next # and if they're equal
        else:
            currNode = currNode.next
    return head

############### Print nth from last in linked list #######################
# it also has 2 approaches - #1- loop upto the length of the linked list and then subract n from len and return the value from front
#2-  Put 2 pointers on the head and loop them till pointer2 reach last. Then return pointer1's value

def getNthFromLast(head,n):
    pointer1= pointer2=head
    for i in range(n): # loop upto last element
        if pointer2 is None:
            return -1 # or none # head.next
        pointer2=pointer2.next # and set pointer2 to 1 position forward to pointer1
    while pointer2: # while pointer 2 loops till the last node
        pointer1=pointer1.next # Move pointer 1 alongside of pointer 2
        pointer2=pointer2.next
    return pointer1.data # return the pointer1's value

############## Partition - Add elements less then the given number to the left of that number and greater than given to right of it.
def partition(ll,x): # x is the given number
    curNode= ll.head
    tail = ll.head
    # Create a linked list with 1 node
    while curNode:
        # while curNode is True
        nextNode= curNode.next # nextNode will be curNode's next value - #### To create a link between curNode and next Node
        curNode.next = None # Set curNode's value to Null
        if curNode.next < x: # if < x
            curNode.next = ll.head # we are adding that node to beginning
            ll.head = curNode # and pointing head to that curNode
        else: # else if > x
            tail.next = curNode # add curNode at last of the linked list
            tail=curNode # Point tail to curNode to establish a connection between curNode and tail.
        curNode= nextNode # continue traversing
    # If the tail's value is not Null, we assign to Null
    if tail.next is not None:
        tail.next = None

# SUM LISTS - Given 2 linked list, we have to add the linked list by taking each node value as digit and return the answer as the linked list
def sumLists(ll1, ll2): # ll1, ll2 are the two linked list
    n1 = ll1.head
    n2 = ll2.head
    # set n1, n2 as the starting nodes of ll1, ll2
    carry = 0 # setting carry =0 to store the carry of the sum
    ll = LinkedList()
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 =n1.next
        else:
            result += n2.value
            n2=n2.next
            # the whole to sum up the nodes of the ll1 and ll2
            ll.add(int(result %10)) # we will add the remainder in the linked list and set the 10's digit/10 to carry
            carry = result/10 # it will save the carry value in variable carry
    return ll # return the llinked list

# Intersection- We have to return the intersection node of the 2 linked lists
# Note - Interecting linked lists are the ll's  which are refrenced to same nodes after a point.
# Intersecting nodes are not based on the node value but instead on node's reference
# Approach - last node must be equal else we will not continue. They are not intersecting nodes.
# we find the shorter and the longer linked list
# we find the length of both linked list and get their difference to ignore the no. of nodes from the longer linked list(if len !=)
# now if shorter node is not longer node (while loop) then traverse till the interection point and return longer node
def intersection(llA, llB):
    if llA.tail is not llB.tail:
        return False
    lenA = len(llA)
    lenB = len(llB)

    shorter= llA if lenA>lenB else llB
    longer= llB if lenA<lenB else llA

    diff = len(longer)-len(shorter)
    longerNode = longer.head
    shorterNode= shorter.head

    for i in range(diff):
        longerNode=longerNode.next

    if shorterNode is not longerNode:
        shorterNode=shorterNode.next
        longerNode=longerNode.next

    return longerNode

    # Helping node for adding the same referenced elements at last
    # Time COmplexity for this algo is O(A+B), A=lenA, B=lenB
def addsameNode(llA,llB,value):
    tempNode = Node() # create a temporary node
    llA.tail.next = tempNode
    llA.tail= tempNode
    llB.tail.next = tempNode
    llA.tail = tempNode

