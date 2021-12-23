# https://adventofcode.com/2021/day/6
from collections import Counter

dataFile = "data.txt"
# dataFile = "test1.txt"
# dataFile = "test2.txt"

fish = []

#make martix from data
with open(dataFile) as file:
  fish = [int(i) for i in file.readline().rstrip().split(",")]
  # fish = Counter(line)


days = 80
for i in range(days):
  for f in range(len(fish)):
    if fish[f] == 0:
      fish.append(8)

    fish[f] -= 1    

    if fish[f] == -1:
      fish[f] = 6

  # print("day", i, fish )
print("count", len(fish))