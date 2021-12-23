# https://adventofcode.com/2021/day/9
# 12:15

from functools import reduce

def printMatrix():
  for r in matrix:
    print(*r, sep="")

def basinsConnected(keepBasin, closeBasin):
  for x in range(len(matrix)):
    row = matrix[x]
    for y in range(len(matrix[x])):
      if basins[closeBasin] == 0:
        return
      if matrix[x][y] == closeBasin:
        matrix[x][y] = keepBasin
        basins[keepBasin] += 1
        basins[closeBasin] -= 1

# return true if 9, otherwise its part of a basin
def markBasins(x,y):
  def getNextBasin():
    b = chr(ord('`')+len(basins)+1)
    basins[b]=0
    return b

  home =  matrix[x][y]

  # 9 are the walls of the basins
  if home == 9:
    return False
  
  up =    matrix[x-1][y] if x > 0  else -1;
  right = matrix[x][y+1] if y + 1 < len(matrix[x]) else -1;
  down =  matrix[x+1][y] if x + 1 < len(matrix) else -1;
  left =  matrix[x][y-1] if y > 0 else -1;

  #seen neighbors marked part of a basin
  points = [up, right, down, left]
  existingBasins = sorted(list(set([p for p in points if isinstance(p, str)])))
  # print("{},{}".format(x,y), home, up, right, down, left, existingBasins)

  if len(existingBasins) == 1:
    matrix[x][y] = existingBasins[0] 
    basins[existingBasins[0]] += 1
  elif len(existingBasins) > 1:    
    # print("basins are connected","{},{}".format(x,y), existingBasins)
    matrix[x][y] = existingBasins[0]
    basins[existingBasins[0]] += 1
    basinsConnected(existingBasins[0], existingBasins[1])
    # print("Replaced {} with {}".format(existingBasins[1], existingBasins[0])) 
  else:
    # all neighbors are numbers at this time, mark self as basin
    # should be any # lower than 9, unless whole map is the same #
    # should always be lower by the time we get here, but as a safty check
    if home < up or home < right or home < down or home < left:
      newBasin = getNextBasin()
      matrix[x][y] = newBasin
      # basins[newBasin[0]] += 1
      basins[newBasin] += 1
    else:
      print("Umm shouldn't be here","{},{}".format(x,y), home, up, right, down, left, existingBasins)

  return True



def areNeighborsHigher(x,y):
  home =  matrix[x][y]
  up =    matrix[x-1][y] if x > 0  else float("inf");
  right = matrix[x][y+1] if y + 1 < len(matrix[x]) else float("inf");
  down =  matrix[x+1][y] if x + 1 < len(matrix) else float("inf");
  left =  matrix[x][y-1] if y > 0 else float("inf");
  
  way1 =  home < up and home < right and home < down and home < left
  
  higherNeighbor = True

  if x == 0: #top row, only check below
    if matrix[x+1][y] <= home:
      higherNeighbor = False  
  elif x == len(matrix)-1: # bottom row, only check above
    if matrix[x-1][y] <= home:
      higherNeighbor = False
  else:
    if matrix[x+1][y] <= home or matrix[x-1][y] <= home:
      higherNeighbor = False

 

  if y == 0: #left side, only check right
    if matrix[x][y+1] <= home:
      higherNeighbor = False  
  elif y == len(matrix[x])-1: #right side, only check left
    if matrix[x][y-1] <= home:
      higherNeighbor = False
  else:
    if matrix[x][y+1] <= home or matrix[x][y-1] <= home:
      higherNeighbor = False

  if way1 != higherNeighbor:
    print("({},{})".format(x,y), matrix[x][y], "xlength", len(matrix), "ylenght", len(matrix[x]))

  return higherNeighbor

  
  # --------------------------------------------------------

basins = {}
matrix = []

dataFile = "data.txt"
# dataFile = "test1.txt"
# dataFile = "test2.txt"
# dataFile = "test3.txt"

with open(dataFile) as file:
  while (line := file.readline().rstrip()):
    matrix.append([int(i) for i in line])

lows = []
for x in range(len(matrix)):
  for y in range(len(matrix[x])):
    if markBasins(x,y):
      basin = ["{},{}".format(x,y), matrix[x][y]]
      # print(basin)
      lows.append(basin)


# print("basins", basins)
top3 = sorted(basins.values())[-3:]
product = reduce((lambda x,y: x * y), top3)
print("TOTAL", product)

# printMatrix()

# for l in lows:
#   print(l[1], l[0])

# print("SUM", sum( [i[1]+1 for i in lows]))
# 1679
# SUM 10460
# PART2 - 1056330