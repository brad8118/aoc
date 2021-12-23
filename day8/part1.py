# https://adventofcode.com/2021/day/8
# 7:30

# NUmber -> segments-> letters
# 0 -> 7 -> abc efg
# 1 -> 2 ->   c  f
# 2 -> 5 -> a cde g
# 3 -> 5 -> a cd fg
# 4 -> 4 -> b cd f
# 5 -> 5 -> ab d fg
# 6 -> 6 -> ab defg
# 7 -> 3 -> a c  f
# 8 -> 7 -> abcdefg
# 9 -> 6 -> abcd fg



correctMap = [
  {"num": "0", "01s":"1110111", "input": "abcefg", "len":7},
  {"num": "1", "01s":"0010010", "input": "abcdefg", "len":7},
  {"num": "2", "01s":"1111111", "input": "abcdefg", "len":7},
  {"num": "3", "01s":"1111111", "input": "abcdefg", "len":7},
  {"num": "4", "01s":"1111111", "input": "abcdefg", "len":7},
  {"num": "5", "01s":"1111111", "input": "abcdefg", "len":7},
  {"num": "6", "01s":"1111111", "input": "abcdefg", "len":7},
  {"num": "7", "01s":"1111111", "input": "abcdefg", "len":7},
  {"num": "8", "01s":"1111111", "input": "abcdefg", "len":7},
  {"num": "9", "01s":"1111111", "input": "abcdefg", "len":7},
]


def createMap(inputSignals, incluePart2):
  # map of letters -> abcdefg contains 1 if input has letter
  converted = [] 

  for signal in inputSignals:
    if not signal: #remove ""
      continue

    usePart1 = 'yes' if len(signal) in [2,4,3,7] else "no"
    if usePart1 == 'no' and not incluePart2: #remove ""
      continue

    singleInputConverted = [0] * 7
    for i, l in enumerate('abcdefg'): 
      if l in signal:
        singleInputConverted[i] = 1
      # letters[i] = 1 if l in signal else 0
      
    converted.append({"01s":singleInputConverted, "input": signal, "part1": usePart1})

  return converted

def printMapings(signals):
  print('part1', 'abcdefg', "input".ljust(9), ": ")

  for row in signals:
    for i in row:
      print(repr(i["part1"]).ljust(5), end=" ")
      print(*i["01s"], sep="", end= " ")
      print(repr(i["input"]).ljust(9), ":")
    print()
 


print("Rules")
validMapping = createMap(["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", 'acf', "abcdefg", "abcdfg"], True)
printMapings([validMapping])

entries = [] # [inputs,  digitals displays]
mappedTo_0_1s = []

# dataFile = "data.txt"
# dataFile = "test1.txt"

with open(dataFile) as file:
  while (line := file.readline().rstrip()):
    row = line.split("|")
    entries.append([row[0].split(" "), row[1].split(" ")])


# print("Display", "1")
# mappedTo_0_1s.append(createMap(entries[0][0], False))
# printMapings(mappedTo_0_1s)

# print("Answers", "1")
# mappedTo_0_1s.append(createMap(entries[0][1], False))
# printMapings(mappedTo_0_1s)


for e in entries:
  mappedTo_0_1s.append(createMap(e[1], False))

printMapings(mappedTo_0_1s)

count =0
for e in mappedTo_0_1s:
  count += len(e)

print("# of part1", count)

