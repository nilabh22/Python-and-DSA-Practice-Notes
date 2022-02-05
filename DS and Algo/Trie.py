# A trie is a tree-based data structure that organizes the information in a hierarchical way.

############ PROPERTIES ############
# 1. It is typically used to store or search strings in a space and time efficient way
# 2. Any node in a Trie can store non repeatitive multiple characters.
# 3. Every Node stores the link of the next character.
# 4. Every Node keeps track of "End of String".

########## Real World Use/Practical Use ############
# 1. Spelling Checker
# 2. Auto Completion feature

class TrieNode:
    def __init__(self):
        self.children= {}
        self.endofString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
# O(1) space and time

############# INSERTION ################

# case 1: A trie is Blank.
# case 2: New string's prefix is common to another string's prefix.
# case 3: New string's prefix is present as complete string.
# case 4: String to be inserted is already present in Trie.

    def insertString(self,word): # Time and Space - O(len(word))
        current = self.root
        for i in word:
            ch =i
            node = current.children.get(ch) # checking if this character (ch) exists in the children or not.
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endofString = True
        print("Successfully Inserted")

############ SEARCHING ############

# case 1: The string doesnot exists in the Trie.
# case 2: String Exists in Trie
# case 3: String is a prefix of another string but it doesnot exists. Ex- searching "AP" in "API".

    def searchString(self,word): #Time = O(len(word)) and space = O(1)
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node
        if currentNode.endofString == True:
            return True
        else:
            return False

############ DELETION ###############
# Deletion always start from bottom node to top, not from top to bottom.
# case 1: Some other prefix of string is same as the the one we want to delete. Ex - ("API", "APPLE"). ##### bottom to top
# case 2: The string is a prefix of another string. Ex - ("API", "APIS"). ########## We set endofString to False for "API"
# case 3: Other string is a prefix of this string. Ex - ("APIS" , "AP")
# case 4: Not any node depends on string.

def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False

    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index + 1)
        return False

    if index == len(word) - 1:
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True

    if currentNode.endofString == True:
        deleteString(currentNode, word, index + 1)
        return False

    canThisNodeBeDeleted = deleteString(currentNode, word, index + 1)
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False


newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")
deleteString(newTrie.root, "App",0)
print(newTrie.searchString("App"))
