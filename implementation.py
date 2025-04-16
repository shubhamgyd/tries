class Node:
  def __init__(self):
    self.links = [None]*26
    self.flag = False
  
  def contains(self, char):
    if self.links[ord(char)-ord("a")] != None:
      return True
    return False
  
  def put(self, char):
    self.links[ord(char)-ord("a")] = Node()
  
  def get(self, char):
    return self.links[ord(char)-ord("a")]

  def end(self):
    self.flag = True
  
  def isEnd(self):
    return self.flag
  

class Trie:
  def __init__(self):
    self.root = Node()
  
  def insert(self, word):
    node = self.root
    for it in word:
      if not node.contains(it):
        node.put(it)
      node = node.get(it)
    node.end()
  
  def search(self, word):
    node = self.root
    for it in word:
      if not node.contains(it):
        return False
      node = node.get(it)
    
    return node.isEnd()
  
  def startsWith(self, word):
    node = self.root
    for it in word:
      if not node.contains(it):
        return False
      node = node.get(it)
    return True


myTrie = Trie()

myTrie.insert("happy")
myTrie.insert("happiness")
print(myTrie.search("happy"))
print(myTrie.startsWith("happ"))
print(myTrie.startsWith("happy"))
