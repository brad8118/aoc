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
  try:
    if type(matrix[y][x]) == str:
      matrix[y][x] = 1
    else:
      matrix[y][x] += 1
  except:
    print("Error", x, y, "Len x (row)", len(matrix[0]), "len y col", len(matrix))

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
    
    # only allow horizonal / vertial lines
    # if start_end[0] != start_end[2] and start_end[1] != start_end[3]: 
    #   continue

    map_size[0] = max(start_end[0], start_end[2], map_size[0])
    map_size[1] = max(start_end[1], start_end[3], map_size[1])

    lines.append(
      {"start": [start_end[0], start_end[1]],
      "end":[start_end[2], start_end[3]]})


for i in range(map_size[1]+1):
  matrix.append(["."]* (map_size[0]+1))

for line in lines:
  #if Xs are the same, add points for the row
  if line["start"][0] == line["end"][0]:
    step = 1 if line["start"][1] < line["end"][1] else -1
    for i in range(line["start"][1], line["end"][1]+ step, step):
      updateMatrixPoint(line["start"][0], i)

 #if Ys are the same, add points for the column
  elif line["start"][1] == line["end"][1] :
    step = 1 if line["start"][0] < line["end"][0] else -1
    for i in range(line["start"][0], line["end"][0]+ step, step):
      updateMatrixPoint(i, line["start"][1])

  #diagonal -- needs to always be 45 degress as always increamenting x & y by 1
  else:
    step_x = 1 if line["start"][0] < line["end"][0] else -1
    step_y = 1 if line["start"][1] < line["end"][1] else -1

    num_of_points = max(
      abs(line["start"][0] - line["end"][0]),
      abs(line["start"][1] - line["end"][1]),
      )+1

    for i in range(num_of_points):
      x = line["start"][0] + (i * step_x)
      y = line["start"][1] + (i * step_y)
      updateMatrixPoint(x,y)

printMatrix()
print("hot spots", calcHotSpots())
