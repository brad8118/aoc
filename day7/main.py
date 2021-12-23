# https://adventofcode.com/2021/day/7
# 4:30am 
# 5:20
# 5:50

from collections import Counter
import math

dataFile = "data.txt"
# dataFile = "test1.txt"

# this needs to be changed - updated accidently
entries = []

#make martix from data
with open(dataFile) as file:
  row = file.readline().rstrip().split("|")
  entries.append([row[0].split(" "), row[1].split(" ")])

counts = Counter(positions)
moves = {}
least_fuel = float('inf')
least_moves = float('inf')

fuel_rate = [0]
for i in range(1, max(counts.keys()) - min(counts.keys()) +1):
  fuel_rate.append(fuel_rate[i-1] + i)

print(fuel_rate)
# 99053143

for num_avg in range(min(counts.keys()), max(counts.keys())+1):
  total_gas = 0
  calc_gas = 0
  for key in counts:
    diff = abs(num_avg - key) 

    #this took ages made the lookup below
    # fuel = 0 
    # for d in range(0, diff+1):
    #   fuel += counts[key] * d
    # total_gas += fuel
    
    total_gas += fuel_rate[diff] * counts[key]
    calc_gas += diff *((diff +1) / 2) * counts[key]

    if total_gas != calc_gas:
      pass

  moves[num_avg] = total_gas
  if total_gas < least_fuel:
    least_fuel=total_gas
    least_moves = num_avg

  

# print(counts)
# print(counts.most_common())
# print(moves)
print("least_moves", least_moves,"least_fuel", least_fuel)

