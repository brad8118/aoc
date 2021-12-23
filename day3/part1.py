# https://adventofcode.com/2021/day/3

dataFile = "data.txt"
# dataFile = "test1.txt"

gamma   =""
epsilon  = ""
forward = 0
matrix = []

#make martix from data
with open(dataFile) as file:
  while (line := file.readline().rstrip()):
    matrix.append(list(line))

# print(matrix)
#loop left to right
for x in range(len(matrix[0])):
  count = 0
  #loop down
  for y in range(len(matrix)):
    # print (x,y, matrix[y][x])
    if matrix[y][x] == "0":
      count -= 1
    else:
      count += 1

  # if count is neg there are more 0s than 1s
  if count < 0:
    gamma += "0"
    epsilon += "1"
  elif count > 0:
    gamma += "1"
    epsilon += "0"
  else:
    raise Exception("Count is 0 -> there's the same # of 0s and 1s -> Oh no")

print("Gamma", gamma, int(gamma, 2), "Epsilon", epsilon, int(epsilon, 2), int(epsilon, 2) *  int(gamma, 2))