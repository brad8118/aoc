# https://adventofcode.com/2021/day/13

dataFile = "data.txt"
# dataFile = "test1.txt"
# dataFile = "test2.txt"
# dataFile = "test3.txt"

lookup = {}
folds = []

def printMatrix(w,d):
  # print(lookup)
  # for y in range(depth+1):  
  #   for x in range(width+1):
  for y in range(d):  
    for x in range(w):
      c = '#' if (x,y) in lookup else "."
      print(c, sep="", end="")
    print()

#only x OR y will be larger zero
def fold(x,y):
  dots_to_remove=[]
  dots_to_add=[]
  for dot in lookup: 
    dot_x, dot_y = dot[0], dot[1]   
    if y != 0:
      if dot_y == y:
        dots_to_remove.append(dot)
      elif dot_y > y:
        dots_to_remove.append(dot)
        new_y = dot_y - y
        new_y = y - new_y
        if new_y >=0:
          dots_to_add.append((dot_x, new_y))
    elif x != 0:
      if dot_x == x:
        dots_to_remove.append(dot)
      elif dot_x > x:
        dots_to_remove.append(dot)
        new_x = dot_x - x
        new_x = x - new_x
        if new_x >=0:
          dots_to_add.append((new_x, dot_y))

  for dot in dots_to_remove:
    del lookup[dot]

  for dot in dots_to_add:
    lookup[dot] = 1
  
with open(dataFile) as file:
  depth, width = 0, 0
  while (line := file.readline().rstrip()):
    x,y = line.split(",")
    x,y = int(x), int(y)
    lookup[(x,y)]=1
    depth = max(depth, y)
    width = max(width, x)

  while (line := file.readline().rstrip()):
    x_or_y, num = line.split("fold along ")[1].split('=')
    folds.append((x_or_y, num))

# print("---Initial--Dots: {}--------".format(len(lookup)))
# printMatrix()

  for f in folds:
    if f[0]=='x':
      fold(int(f[1]), 0)
      width = int(f[1])
    else:
      fold(0, int(f[1]))
      depth = int(f[1])

    # print(len(lookup))

  # print("-----------Dots: {}--------".format(len(lookup)))
  printMatrix(width, depth)



# print(lookup)
print("-----------------------")
# print(folds)


