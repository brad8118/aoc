# https://adventofcode.com/2021/day/3
# https://adventofcode.com/2021/day/3#part2

dataFile = "data.txt"
# dataFile = "test1.txt"

matrix = []

#make martix from data
with open(dataFile) as file:
  while (line := file.readline().rstrip()):
    matrix.append(list(line))

org_matrix = matrix

results = {}
types = ["oxygen", "CO2"]

for gasType in types: 
  #loop to the rigth
  for x in range(len(matrix[0])):
    
    if len(matrix) == 1:
      break

    ones = []
    zeros = []

    #loop down
    for y in range(len(matrix)):
      if matrix[y][x] == "0":
        zeros.append("".join(matrix[y]))
      else:
        ones.append("".join(matrix[y]))

    # oxygen == most
    # CO2 == least
    if len(ones) == len(zeros):
      matrix = ones if gasType == "oxygen" else zeros
    elif len(ones) > len(zeros):
      matrix = ones if gasType == "oxygen" else zeros
    else:
      matrix = zeros if gasType == "oxygen" else ones

    print("0s", len(zeros), zeros)
    print("1s", len(ones), ones)
    print("-----------------------")

  print("========================")
  results[gasType] = matrix[0]
  matrix = org_matrix 

print(results, int(results["oxygen"], 2), int(results["CO2"], 2), int(results["oxygen"], 2) * int(results["CO2"], 2) ) 



