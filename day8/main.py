# https://adventofcode.com/2021/day/8
# 7:30

def printKeyValue(dicts):
  print(*dicts.keys(), sep="")
  print(*dicts.values(), sep="")

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
      
    converted.append({"01s":singleInputConverted, "input": "".join(sorted(signal)), "part1": usePart1, "len": len(signal)})

  return converted

def printMapings(signals):
  # print("+++++++++++++")
  # print(signals)
  totals = [0] * 7
  print('part1', 'abcdefg', "input".ljust(9), ":", "len")
  for s in signals:   
    print(repr(s["part1"]).ljust(5), end=" ")
    print(*s["01s"], sep="", end= " ")
    print(repr(s["input"]).ljust(9), ":", repr(s["len"]).ljust(3))
  
    for i, num in enumerate(s["01s"]):
      totals[i] += int(num)

  print(' a b c d e f g')  
  for i in totals:
    print(repr(i).rjust(2), sep="", end="")


  
  print()
 

# NUmber -> segments-> letters
# 0 -> 6 -> abc efg
# 1 -> 2 ->   c  f
# 2 -> 5 -> a cde g
# 3 -> 5 -> a cd fg
# 4 -> 4 -> b cd f
# 5 -> 5 -> ab d fg
# 6 -> 6 -> ab defg
# 7 -> 3 -> a c  f
# 8 -> 7 -> abcdefg
# 9 -> 6 -> abcd fg

# if set([mapping['a'], mapping['g']]) <= set(num["input"].split()):


def createRuleLookup(signals):
  indexToLetterLookup = ['a','b','c','d','e','f','g']
  mapping = {'a':' ', 'b':' ','c':' ', 'd':' ', 'e':' ', 'f':' ', 'g':' ' } 
  # mapping = {} 

  totals = [0] * 7
  for num in signals:
    for i, num in enumerate(num["01s"]):
      totals[i] += int(num)

  # f=9, b=6, e=4
  for i, num in enumerate(totals):
    if num == 9:
      mapping['f'] = indexToLetterLookup[i]
    elif num == 6:
      mapping['b'] = indexToLetterLookup[i]
    elif num == 4:
      mapping['e'] = indexToLetterLookup[i]

    # print(repr(i).rjust(2), sep="", end="")

  # print("afterInit")
  # printKeyValue(mapping)


  one = list(filter(lambda x: x['len'] == 2, signals))[0]
  four = list(filter(lambda x: x['len'] == 4, signals))[0]
  seven = list(filter(lambda x: x['len'] == 3, signals))[0]
  eight = list(filter(lambda x: x['len'] == 7, signals))[0]
  zero, two, three, five, six, nine = 0, 0, 0, 0, 0, 0

  #unique lengths
  ## figure out top "a"
  # num -> len
  # 1 -> 2  0010010 'cf' 
  # 7 -> 3  1010010 'acf'
  for letter in seven["input"]:
    if letter not in one["input"]:
      mapping['a'] = letter


  # print("before c")
  # printKeyValue(mapping)
  # print("one", one)
  for l in one["input"]:
    if l not in mapping.values():
      mapping['c'] = l

  # already have b,c,f get center d
  for l in four["input"]:
    if l not in mapping.values():
      mapping['d'] = l

  # print("after c")
  # printKeyValue(mapping)
  # for num in [one, four,seven,eight]:
  #   print(*num["01s"], sep="")

  ## figure out bottom "g"
  # c is common in all 4 #s
  # for i in range(8):
  #   if one['01s'][i] and four['01s'][i] and seven['01s'][i] and eight['01s'][i]:
  #     mapping['g'] = indexToLetterLookup[i]
  #     break

  # # figure out middle "d"
  # # filter by 5-> 2,3,5 
  # # look for #3, then find letter not in #1, but has keys A & G
  # for num in filter(lambda x: x['len'] == 5, signals):
  #   print("num", num['input'], "one", one["input"], "mapping", mapping)
  #   if set(list(one['input'])) <= set(list(num['input'])):
  #     for l in num["input"]:
  #       if l not in one['input'] and l not in mapping.values():
  #         mapping['d'] = l
  #         three = num
  #         break
      

  # # look for right top "c" & bottom left "e"
  # # loop #s with 6 -> 0,6,9
  # for num in filter(lambda x: x['len'] == 6, signals):
  #   # print("num", num['input'], "one", one["input"], "d", mapping['d'])
  #   if set(list(one['input'])) <= set(list(num['input'])):
  #     #already know middle 'd' which is not in #0

  #     if mapping['d'] in num['input']:
  #       nine = num       
  #     else:
  #       zero = num
  #   else:
  #     #6 doesn't have "c" but #1 does
  #     six = num

  # for l in one['input']:
  #   if l in six['input']:
  #     mapping['f'] = l
  #   else:
  #     mapping['c'] = l

  # # get "e", using 8 & 9
  # for l in eight['input']:
  #   if l not in nine['input']:
  #     mapping['e'] = l
  #     break


  # g is the last letter, so check the mappings
  for key in mapping.keys():
    if key not in mapping.values():
      mapping['g'] = key

  # print("mapping", mapping)
  # for k, v in mapping.items():
  #   print(k,v)
  # print(*sorted(mapping.values()), sep="")

  #not sure why I didn't flip the dict
  lookup = {}
  for k,v in mapping.items():
    lookup[v] = k

  return lookup 


def translateSignal(translator, lstSignals):
  lettersToDigitalLookup = {"abcefg":"0", "cf":"1", "acdeg":"2", "acdfg":"3", "bcdf":"4", "abdfg":"5", "abdefg":"6", 'acf':"7", "abcdefg":"8", "abcdfg":"9"}

  translated = []
  for signal in lstSignals:
    s = "".join(sorted([translator[l] for l in signal]))
    try:
      lettersToDigitalLookup[s]
    except Exception as e:
      print("Missing", s)
    translated.append([s, lettersToDigitalLookup[s]])

  return translated

# --------------------------------------------------------------------
print("Rules")
validMapping = createMap(["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", 'acf', "abcdefg", "abcdfg"], True)
printMapings(validMapping)
print("--------------------------------------------")

rows = [] # [inputs,  digitals displays]
mappedTo_0_1s = []
answers_0_1s = []

# dataFile = "data.txt"
dataFile = "test1.txt"
# dataFile = "test2.txt"
# dataFile = "test3.txt"

with open(dataFile) as file:
  while (line := file.readline().rstrip()):
    row = line.split(" | ")
    rows.append([row[0].split(" "), row[1].split(" ")])

total = 0
for r in rows:
  inputSignalObjs = createMap(r[0], True)
  printMapings(inputSignalObjs)
  translor = createRuleLookup(inputSignalObjs)
  translatedOuputs = translateSignal(translor, r[1])
  # print(translatedOuputs)
  stringedDigitalOuts = "".join([to[1] for to in translatedOuputs])
  print (stringedDigitalOuts)
  total += int(stringedDigitalOuts)

print("GRAND TOTAL", total)

# print("Answers", "1")
# answers_0_1s.append(createMap(rows[0][1], True))
# printMapings(answers_0_1s)

# createRuleLookup(mappedTo_0_1s[0])

# for e in rows:
#   mappedTo_0_1s.append(createMap(e[1], False))

# printMapings(mappedTo_0_1s)

# count =0
# for e in mappedTo_0_1s:
#   count += len(e)

# print("# of part1", count)

