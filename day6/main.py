# https://adventofcode.com/2021/day/6
from collections import Counter

dataFile = "data.txt"
# dataFile = "test1.txt"

fish ={}

#make martix from data
with open(dataFile) as file:
  fish = [int(i) for i in file.readline().rstrip().split(",")]
  fish = Counter(fish)

days = 256
for day in range(days):
  previous_fish = 0
  for i in range(8, -1, -1):
    if i == 0 :
      fish[8] = fish[0] 
      fish[6] += fish[0]      
      fish[0] = previous_fish
    else:
      tmp = fish[i] 
      fish[i] = previous_fish
      previous_fish = tmp

print("count", sum(fish.values()))
