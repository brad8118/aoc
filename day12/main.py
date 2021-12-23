# https://adventofcode.com/2021/day/12
# https://www.redblobgames.com/pathfinding/a-star/introduction.html

from collections import deque

class AOC_2021_day12:
  def __init__(self):
    self.nodes = {}
  
  def readFile(self):
    # dataFile = "data.txt"
    dataFile = "test1.txt"
    # dataFile = "test2.txt"

    with open(dataFile) as file:
      while (line := file.readline().rstrip()):
        node, child = line.split('-')
        
        if node in self.nodes:
          self.nodes[node].append(child)
        else:
          self.nodes[node] = [child]


  def part1(self):
    visited = [] 
    to_visit = deque()
    to_visit.append("start")
    more_to_visit = True

    while more_to_visit:
      new_path = []
      for p in to_visit:
        for c in self.nodes[p]
          if c == "end":
            visited.append


      node = self.nodes.popLeft()
      path.append(node)
      
      if node not in path:
        pass
    if:

    else:
      more_to_visit= False

aoc = AOC_2021_day12()
aoc.readFile()
aoc.part1()



