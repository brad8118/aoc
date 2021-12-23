# https://adventofcode.com/2021/day/9
# 12:15

def areNeighborsHigher(x,y):
  home =  matrix[x][y]
  up =    matrix[x-1][y] if x > 0  else float("inf");
  right = matrix[x][y+1] if y + 1 < len(matrix[x]) else float("inf");
  down =  matrix[x+1][y] if x + 1 < len(matrix) else float("inf");
  left =  matrix[x][y-1] if y > 0 else float("inf");

  return home < up and home < right and home < down and home < left
  
  # higherNeighbor = True
  # if y== len(matrix[x])-1:
  #   print(x,y, matrix[x][y], "xlength", len(matrix), "ylenght", len(matrix[x]))

  # if x == 0: #top row, only check below
  #   if matrix[x+1][y] < home:
  #     higherNeighbor = False  
  # elif x == len(matrix)-1: # bottom row, only check above
  #   if matrix[x-1][y] < home:
  #     higherNeighbor = False
  # else:
  #   if matrix[x+1][y] < home or matrix[x-1][y] < home:
  #     higherNeighbor = False

 

  # if y == 0: #left side, only check right
  #   if matrix[x][y+1] < home:
  #     higherNeighbor = False  
  # elif y == len(matrix[x])-1: #right side, only check left
  #   if matrix[x][y-1] < home:
  #     higherNeighbor = False
  # else:
  #   if matrix[x][y+1] < home or matrix[x][y-1] < home:
  #     higherNeighbor = False

  # return higherNeighbor
  
  # --------------------------------------------------------


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
    if areNeighborsHigher(x,y):
      lows.append(["{},{}".format(x,y), matrix[x][y]])

for l in lows:
  print(l[1], l[0])

print("SUM", sum( [i[1]+1 for i in lows]))
# 1679
# SUM 10460