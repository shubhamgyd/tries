from sys import *
from collections import *
from math import *

from typing import *

class Node:
    def __init__(self):
        self.links = [None]*26
        self.flag = False
    
    def contains(self, char):
        return self.links[ord(char)-ord("a")] != None
    
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
    
    def allPrefixCheck(self, word):
        node = self.root
        for it in word:
            if node.contains(it):
                node = node.get(it)
                if not node.isEnd():
                    return False
            else:
                return False
        return True



def completeString(n: int, a: List[str])-> str:
    myTrie = Trie()
    for i in range(n):
        myTrie.insert(a[i])
    
    longest = ""
    for i in range(n):
        if myTrie.allPrefixCheck(a[i]):
            if len(longest) < len(a[i]):
                longest = a[i]
            elif len(longest) == len(a[i]):
                longest = min(longest, a[i])
    if longest == "": return None
    return longest

N = 4
A = [ "ab" , "abc" , "a" , "abcd", "abce" ]
print(completeString(N, A))