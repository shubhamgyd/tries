class Node:
  def __init__(self, ):
    self.links = [None]*26
    self.cntPrefix = 0
    self.cntEnd = 0
  
  def contains(self, char):
    return self.links[ord(char)-ord("a")] != None
  
  def put(self, char):
    self.links[ord(char)-ord("a")] = Node()
  
  def get(self, char):
    return self.links[ord(char)-ord("a")]
  
  def increasePrefix(self,):
    self.cntPrefix += 1
  
  def decreasePrefix(self, ):
    self.cntPrefix -= 1
  
  def increaseCntEnd(self, ):
    self.cntEnd += 1
  
  def decreaseCntEnd(self, ):
    self.cntEnd -= 1
  
  def getTotalCnt(self):
    return self.cntEnd
  
  def getTotalPrefixCnt(self):
    return self.cntPrefix
  
class Trie:
  def __init__(self):
    self.root = Node()
  
  def insert(self, word):
    node = self.root
    for it in word:
      if not node.contains(it):
        node.put(it)
      node = node.get(it)
      node.increasePrefix()
    node.increaseCntEnd()
  
  def countOfWord(self, word):
    node = self.root
    for it in word:
      if not node.contains(it):
        return 0
      node = node.get(it)
    return node.getTotalCnt()
  
  def countOfStartsWithWord(self, word):
    node = self.root
    for it in word:
      if not node.contains(it):
        return 0
      node = node.get(it)
    return node.getTotalPrefixCnt()
  
  def eraseWord(self, word):
    node = self.root
    for it in word:
      if not node.contains(it):
        return
      node = node.get(it)
      node.decreasePrefix()
    node.decreaseCntEnd()
    return f"Deletion of word \"{word}\" is successfull"


myTrie = Trie()

myTrie.insert("happy")
myTrie.insert("happy")
myTrie.insert("happiness")
print("Total number of word \"happy\": ",myTrie.countOfWord("happy"))
print(myTrie.eraseWord("happy"))
print("Total number of word \"happy\": ",myTrie.countOfWord("happy"))
print("Total number of words starts with \"happ\"",myTrie.countOfStartsWithWord("happ"))
# print(myTrie.startsWith("happy"))