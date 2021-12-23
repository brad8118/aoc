# https://adventofcode.com/2021/day/7
# 4:30am

from collections import Counter

dataFile = "data.txt"
# dataFile = "test1.txt"

positions = []

#make martix from data
with open(dataFile) as file:
  positions = [int(i) for i in file.readline().rstrip().split(",")]

counts = Counter(positions)
moves = {}
least_fuel = float('inf')
least_moves = float('inf')

for num_avg, occurrences_avg in counts.items():
  total_gas = 0
  for key in counts:
    diff = abs(num_avg - key) 
    fuel = counts[key] * diff
    total_gas += fuel

  moves[num_avg] = total_gas
  if total_gas < least_fuel:
    least_fuel=total_gas
    least_moves = num_avg

  

# print(counts)
print(counts.most_common())
print(moves)
print("least_moves", least_moves,"least_fuel", least_fuel)

