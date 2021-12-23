# https://adventofcode.com/2021/day/2
# https://adventofcode.com/2021/day/2#part2

data = "data.txt"
# data = "test1.txt"

up_down = 0
forward = 0
up =0
down =0

with open(data) as file:
  while (line := file.readline().rstrip().split(' ')):
    if(line[0] ==""):
      break
    if line[0] == "forward":
      forward += int(line[1])
    elif line[0] == "down":
      up_down -= int(line[1])
      down +=int(line[1])
    else:
      up_down += int(line[1])
      up +=int(line[1])

    print("forward", forward,  "up", down, "down", up, "up_down", up_down, "X", abs( forward * up_down), line)   

# print("forward", forward, "up_down", up_down, "X", forward * up_down)
	# measurements = [int(line.rstrip()) for line in file]
