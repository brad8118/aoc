# https://adventofcode.com/2021/day/14
from collections import Counter

class Node:
  def __init__(self, previous, letter, nextNode=None):
    self.previous = previous
    self.letter = letter
    self.next = nextNode

class AOC_2021_day14:
  def __init__(self):
    self.head= None
    self.tail= None
    self.counts = Counter()
    self.mapping = {}
    # The correct way... arrr --
    self.part2PairCounts = Counter()
    self.part2LetterCounts = Counter()


  def printList(self):
    node = self.head
    while(node):
      print(node.letter, sep="", end="")
      node = node.next
    print()
  
  def addNode(self, prev, letter, nextNode):   
    self.counts[letter] += 1 
    node = Node(prev, letter, nextNode)
    if prev:
      prev.next = node
    if nextNode:
      nextNode.previous = node    
    if prev == None:
      self.head = node    
    if nextNode == None:
      self.tail = node
    # self.printList()
    return node

  def readFile(self):
    dataFile = "data.txt"
    # dataFile = "test1.txt"
    # dataFile = "test2.txt"

    with open(dataFile) as file:
      while (line := file.readline().rstrip()):
        prev = None
        pairedLetters = ""
        for l in line:
          prev = self.addNode(prev,l, None)
          pairedLetters = pairedLetters[-1:] + l
          # part2
          self.part2LetterCounts[l] += 1
          if len(pairedLetters) ==2:
            self.part2PairCounts[pairedLetters] +=1
      
      # self.printList()
      while (line := file.readline().rstrip()):
        key, value = line.split(" -> ")
        self.mapping[key] = value
      
      print("input")
      self.printList()
      print("---------------------")

  def part1(self, loopCount):
    print("-----PART1---------")
    for i in range(loopCount):
      leftNode = self.head
      while(leftNode.next):
        rightNode = leftNode.next
        combined = leftNode.letter + rightNode.letter
        if combined in self.mapping:
          self.addNode(leftNode,self.mapping[combined], rightNode)
        leftNode = rightNode
    
      # self.printList()

    print("getting counts") 
    most = self.counts.most_common()[0]
    least = self.counts.most_common()[:-2:-1][0]
    print("most", most) 
    print("lease",  least)
    print("Answer", most[1]- least[1])
    print("-----PART1---------")
    

  def part2(self, loopCount):
    print("-----PART2---------")
    for i in range(loopCount):
      newItemsToAdd = Counter()
      for key in self.mapping: 
        numOfPairs =  0 if key not in self.part2PairCounts else self.part2PairCounts[key]
        if numOfPairs > 0:
          newItemsToAdd[key[0]+ self.mapping[key]] += numOfPairs
          newItemsToAdd[self.mapping[key] + key[1]] += numOfPairs
          # newItemsToAdd[key] = numOfPairs *-1
          self.part2PairCounts[key] = 0
          self.part2LetterCounts[self.mapping[key]] += numOfPairs
          
      # print("NewPairs", newItemsToAdd)
      self.part2PairCounts.update(newItemsToAdd)
      # print(self.part2LetterCounts)
      # print(self.part2PairCounts)


    print("getting counts") 
    most = self.part2LetterCounts.most_common()[0]
    least = self.part2LetterCounts.most_common()[-1:][0]
    print("most", most) 
    print("lease",  least)
    print("Answer", most[1]- least[1])
    print("-----PART2---------")
    # 3528317079545
 
aoc = AOC_2021_day14()
aoc.readFile()
# aoc.part1(5)
# aoc.printList()
aoc.part2(40)

  