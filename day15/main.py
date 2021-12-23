# https://adventofcode.com/2021/day/15

from collections import Counter
from datetime import datetime, timedelta
import queue

class AOC_2021_day15:
  def __init__(self):
    self.matrix = []
    self.shortestRoute = float("inf")
  
  def getEnd(self):
    return (len(self.matrix[0]) -1, len(self.matrix)-1)

  def printMatrix(self):
    width, depth = self.getEnd()
    for y in range(depth+1):
      for x in range(width+1):
        print(self.matrix[y][x], sep="", end="")
      print()

  def printDict(self, d):
    for k,v in d.items():
      print("{}:{}".format(k,v), sep=", ", end=" ")
    print()

  def readFile(self):
    # dataFile = "data.txt"
    dataFile = "test1.txt"
    # dataFile = "test2.txt"

    with open(dataFile) as file:
      while (line := file.readline().rstrip()):
        self.matrix.append([int(n) for n in line])

  def getNeighbors(self, point):
    x,y = point[0], point[1]
    possible_neighbors =[(x-1,y), (x+1, y), (x, y-1), (x,y+1)]
    neighbors = []
    for n in possible_neighbors:
      x,y = n[0], n[1]
      if (x >=0 and x < len(self.matrix[0]) and 
        y >=0 and y < len(self.matrix)):
        neighbors.append(n)

    # print("P", point, neighbors)
    return neighbors
    
  def part2(self, sizeIncrease):
    width, depth = self.getEnd()[0]+1, self.getEnd()[1]+1 
    # print("width", width, "depth", depth)

    #multiple rows across
    for y in range(depth): 
      orginal_row = self.matrix[y]  
      for i in range(1, sizeIncrease):               
        new_items_for_row = [p+i-9 if p + i > 9 else p + i for p in orginal_row]
        self.matrix[y] = [*self.matrix[y], *new_items_for_row]

    #multiple rows down    
    for i in range(1, sizeIncrease):  
      for y in range(depth):          
        new_row = [p+i-9 if p + i > 9 else p + i for p in self.matrix[y]]
        self.matrix.append(new_row)

    # width, depth = self.getEnd()[0]+1, self.getEnd()[1]+1  
    # print("width", width, "depth", depth)
    # self.printMatrix()
    
  def calcPriority(self, p):
    end = self.getEnd()
    return abs(end[0] - p[0]) + abs(end[1] - p[1])

  def part1(self,start):
    start_time = datetime.now()

    # nodes_to_search = set([start])
    nodes_to_search = queue.PriorityQueue()
    nodes_to_search.put((0, start))
    visited = {}
    visited[start]= 0
    # cost={}
    # cost[start]=0

    while nodes_to_search:
      # current = nodes_to_search.pop()
      current = nodes_to_search.get()[1]
      # print(current)
      for n in self.getNeighbors(current):
        # print("c", current, "n",n, self.printDict(visited))
        # new_cost = cost[current] + self.matrix[n[1]][n[0]] # maxtrix[y][x]
        new_cost = visited[current] + self.matrix[n[1]][n[0]] # maxtrix[y][x]
        end_cost=  float("inf") if self.getEnd() not in visited else visited[self.getEnd()]    
        # end_cost=  float("inf")
        if new_cost < end_cost and (n not in visited or new_cost < visited[n]):
          # cost[n]=new_cost
          nodes_to_search.put((self.calcPriority(current), n))          
          visited[n]=  new_cost # doesn't matter what the value is

    
    end = datetime.now()

    # self.printMatrix() 
    print("TIME:", end-start_time)   
    print("Part1 - Cost", visited[self.getEnd()] )
    # print("Part1", min(cost.values()))
    # self.printDict(cost)

aoc = AOC_2021_day15()
aoc.readFile()
aoc.part2(5)
aoc.part1((0,0))


