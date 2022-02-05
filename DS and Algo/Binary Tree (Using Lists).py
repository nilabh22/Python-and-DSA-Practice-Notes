################ Creation of a Bianry tree using Python Lists ###################

class BinaryTree:
    def __init__(self,size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, value):
        if self.lastUsedIndex+1 == self.maxSize:
            return "The BT is already full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex+=1
        return "The value has been successfully inserted"

    def searchBT(self,nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Node has been found"
        return "Node doesn't exist in the Tree"



newBT = BinaryTree(8)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
print(newBT.searchBT("Hot"))