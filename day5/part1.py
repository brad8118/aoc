# https://adventofcode.com/2021/day/5
# 8:55

dataFile = "data.txt"
# dataFile = "test1.txt"
# dataFile = "test2.txt"

map_size = [0,0]
lines = []
matrix = []

def printMatrix():
  for row in matrix:
    print(*row, sep ='')

def updateMatrixPoint(x,y):
  if type(matrix[x][y]) == str:
    matrix[x][y] = 1
  else:
    matrix[x][y] += 1

def calcHotSpots():
  hot_spots = 0
  for row in matrix:
    for point in row:
      if type(point) == int and point > 1:
        hot_spots += 1
  return hot_spots

with open(dataFile) as file:
  while (line := file.readline().rstrip()):
    start_end = [int(s) for s in line.replace(" -> ",",").split(",")]
    
    #only allow horizonal / vertial lines
    if start_end[0] != start_end[2] and start_end[1] != start_end[3]: 
      # print("Not valid", start_end)
      continue

    map_size[0] = max(start_end[0], start_end[2], map_size[0])
    map_size[1] = max(start_end[1], start_end[3], map_size[1])

    lines.append(
      {"start": [start_end[0], start_end[1]],
      "end":[start_end[2], start_end[3]]})


for i in range(map_size[1]+1):
  matrix.append(["."]* (map_size[0]+1))

# for i in range(4, 10):
#       print(i, end=" ")
# for i in range(10, 4):
#       print(i, end=" ")

for line in lines:
  #if Xs are the same, add points for the row
  if line["start"][0] == line["end"][0]:
    step = 1 if line["start"][1] < line["end"][1] else -1
    for i in range(line["start"][1], line["end"][1]+ step, step):
      updateMatrixPoint(i, line["start"][0])

 #if Ys are the same, add points for the column
  elif line["start"][1] == line["end"][1] :
    step = 1 if line["start"][0] < line["end"][0] else -1
    for i in range(line["start"][0], line["end"][0]+ step, step):
      updateMatrixPoint(line["start"][1], i)

  # start_x = line["start"][0] 
  # end_x = line["end"][0] 

  # start_y = line["start"][1] 
  # end_y = line["end"][1] 

  # print(start_x, start_y, end_x, end_y, "::", start_x - end_x, start_y - end_y)


printMatrix()
print(calcHotSpots())
# print(lines)