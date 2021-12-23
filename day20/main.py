# https://adventofcode.com/2021/day/20

class AOC_2021_day20:
  def __init__(self):
    self.lookup=""
    self.points_of_light={}

  def printMatrix(self):
    min_max = self.getMinMax()
    for y in range(min_max['y'][0] , min_max['y'][1]+1):
      for x in range(min_max['x'][0] , min_max['x'][1]+1):
        print(self.points_of_light.get((x,y),'.'), sep="", end="")
      print()
    print("---------------")


  def getMinMax(self):
    Xs = []
    Ys = []
    for k in self.points_of_light:
      # if self.points_of_light[k] == "1":
      Xs.append(k[0])
      Ys.append(k[1])

    min_max = {'x':[min(Xs),max(Xs)], 'y':[min(Ys),max(Ys)]}
    return min_max

  def readFile(self, file):
    with open(dataFile) as file:
      while (line := file.readline().rstrip()):
        self.lookup = line

      #Xs are left to right(rows), Ys are up and down (Columns)
      depth=-1
      while (line := file.readline().rstrip()):  
        depth +=1
        for y, n in enumerate(line):
          # print(y,depth, n)
          if n == "#":
            self.points_of_light[(y, depth)]="1"

    # print("Points of Light : Import", self.points_of_light)

  def getEnhancedPixel(self, bin_num):
    enhanced = self.lookup[int(bin_num,2)]
    enhanced = "1" if enhanced == "#" else "0"
    return enhanced

  def getBinayNeighbors(self, point):
    x,y = point
    neighbors = [
      (x-1, y-1), (x, y-1), (x+1, y-1),
      (x-1, y),   (x, y),   (x+1, y),
      (x-1, y+1), (x, y+1), (x+1, y+1)
      ]

    binary_num = ""
    for p in neighbors:
      binary_num += self.points_of_light.get(p, "0")
    return binary_num


  def part1(self, enhancementCount):    
    # self.printMatrix()
    print("Part1", len(self.points_of_light))

    for count in range(enhancementCount):
      min_max = self.getMinMax()
      print(min_max)
      changes = {}
      for y in range(min_max['y'][0] -1, min_max['y'][1]+2):
        for x in range(min_max['x'][0] -1, min_max['x'][1]+2):
          bin_num = self.getBinayNeighbors((x,y))
          enhanced_pixel = self.getEnhancedPixel(bin_num)
          changes[(x,y)]=enhanced_pixel

      # print("Changes", self.points_of_light)

      for k,v in changes.items():
        if v == "0":
          if k in self.points_of_light:
            del self.points_of_light[k]
        else:
          self.points_of_light[k] = v

      # self.printMatrix()

    # print("Points of Light", self.points_of_light)
    print("Part1", len(self.points_of_light))
    # 5129 ish.. to low
    # 5394 too high 5393

dataFile = "data.txt"
# dataFile = "test1.txt"
# dataFile = "test2.txt"

aoc = AOC_2021_day20()
aoc.readFile(dataFile)
aoc.part1(2)
# aoc.part2()