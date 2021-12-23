# https://adventofcode.com/2021/day/11
dataFile = "data.txt"
# dataFile = "test1.txt"
# dataFile = "test2.txt"
# dataFile = "test3.txt"

matrix = []
lookup = {}
width = 0
depth = -1
flash_count = 0
increases_this_step = {}

def printMatrix():
  for x in range(depth):
    for y in range(width):
      print(lookup[(x,y)], sep="", end="")
    print()


def increaseSelf(x,y):
  if (x,y) not in lookup:
    return

  if (x,y) not in increases_this_step:
    lookup[(x,y)] += 1

  # print("increase", (x,y), lookup[(x,y)])
  if lookup[(x,y)] == 10:
    increases_this_step[(x,y)]=0
    lookup[(x,y)] = 0

    neighbors = [
      (x-1, y), (x+1, y), # above & below
      (x, y-1), (x, y+1), # left & right
      (x-1, y-1), (x-1, y+1), # diag above
      (x+1, y-1), (x+1, y+1)  # diag below
      ]

    for n in neighbors:
      increaseSelf(n[0], n[1])



with open(dataFile) as file:
  while (line := file.readline().rstrip()):
    depth += 1
    width = len(line)
    for y, n in enumerate(line):
      # print(depth, y, n)
      lookup[(depth,y)]=int(n)
depth += 1



for loop in range(2000000):
  # print("Search", loop)
  # printMatrix()
  for x in range(depth):
    for y in range(width):
      increaseSelf(x,y)

      #change all #s above 9 to 0
  flash_count += len(increases_this_step)
  if len(increases_this_step) == len(lookup) and loop > 0:
    print("All Flashed", loop)
    break
  increases_this_step = {}
  


print("-----------------------")
printMatrix()
print(flash_count)
