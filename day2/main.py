# https://adventofcode.com/2021/day/2
# https://adventofcode.com/2021/day/2#part2

data = "data.txt"
# data = "test1.txt"

aim =0
up_down = 0
forward = 0


with open(data) as file:
  while (line := file.readline().rstrip().split(' ')):
    if(line[0] ==""):
      break
    if line[0] == "forward":
      forward += int(line[1])
      up_down -= aim * int(line[1])
    elif line[0] == "down":
      # up_down -= int(line[1])
      aim += int(line[1])
    else:
      # up_down += int(line[1])
      aim -= int(line[1])

    # print("aim", aim,"forward", forward,  "up", down, "down", up, "up_down", up_down, "X", abs( forward * up_down), line)   
    print("aim", aim,"forward", forward, "up_down", up_down, "X", abs( forward * up_down), line )   

# print("forward", forward, "up_down", up_down, "X", forward * up_down)
	# measurements = [int(line.rstrip()) for line in file]
