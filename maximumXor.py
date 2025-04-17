class Node:
  def __init__(self):
    self.links = [None, None]
  
  def contains(self, bit):
    return self.links[bit] != None
  
  def put(self, bit):
    self.links[bit] = Node()
  
  def get(self, bit):
    return self.links[bit]

class Trie:
  def __init__(self):
    self.root = Node()
  
  def insert(self, num):
    node = self.root
    for i in range(31, -1, -1):
      bit = (num >> i) & (1)
      if not node.contains(bit):
        node.put(bit)
      node = node.get(bit)
  
  def getMax(self, num):
    node = self.root
    maxi = 0
    for i in range(31, -1, -1):
      bit = (num >> i) & 1
      if node.contains(1-bit):
        maxi = maxi | (1 << i)
        node = node.get(1-bit)
      else:
        node = node.get(bit)
    return maxi

myTrie = Trie()
arr = [3, 10, 5, 25, 2]
for i in range(len(arr)):
  myTrie.insert(arr[i])

print(myTrie.getMax(8))

'''
3  -> 00011 ^ 01000 => 01011 => 11
10 -> 01010 ^ 01000 => 00010 => 2
5  -> 00101 ^ 01000 => 01101 => 13
25 -> 11001 ^ 01000 => 10001 => 17
2  -> 00010 ^ 01000 => 01010 => 10

8  -> 01000

So, the maximum xor is 17 of 8 and one of element of arr i.e 25
'''
