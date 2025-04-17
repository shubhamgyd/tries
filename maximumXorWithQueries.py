class Node:
  def __init__(self,):
    self.links = [None, None]
  
  def contains(self, bit):
    return self.links[bit] != None
  
  def put(self, bit):
    self.links[bit] = Node()

  def get(self, bit):
    return self.links[bit]

class Trie:
  def __init__(self,):
    self.root = Node()
  
  def insert(self, num):
    node = self.root
    for i in range(31, -1, -1):
      bit = (num>>i) & 1
      if not node.contains(bit):
        node.put(bit)
      node = node.get(bit)
  
  def getMax(self, num):
    node = self.root
    maxi = 0
    for i in range(31, -1, -1):
      bit = (num>>i) & 1
      if node.contains(1-bit):
        maxi = maxi | (1<<i)
        node = node.get(1-bit)
      else:
        node = node.get(bit)
    return maxi

class Solution:
  def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
    offlineQueries = []
    j = 0
    for i in range(len(queries)):
      x, m = queries[i]
      offlineQueries.append((m, (x, i)))
    nums.sort()
    offlineQueries.sort(key=lambda x: x[0])

    myTrie = Trie()
    i = 0
    n = len(nums)
    ans = [-1 for i in range(len(queries))]

    for m, it in offlineQueries:
      while i < n and nums[i] <= m:
        myTrie.insert(nums[i])
        i += 1
      if i == 0:
        continue
      else:
        ans[it[1]] = myTrie.getMax(it[0])
    
    return ans
      