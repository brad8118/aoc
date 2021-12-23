

dataFile = "data.txt"
# dataFile = "test1.txt"
# dataFile = "test2.txt"
# dataFile = "test3.txt"

chunks= []


from statistics import median

def p2s(l):
	scores = {')':1, ']':2, '}':3, '>':4}
	s = 0
	for c in l:
		s = s*5+scores[c]
	return s

with open(dataFile) as file:
  while (line := file.readline().rstrip()):
    chunks.append(line)

sum_bad_closing = {']':0, '}':0,')':0, '>':0 }
lookup = {'{':'}', '[':']','<':'>', '(':')'}

summed = 0
incompletes = []
needs = {"(":")","{":"}","<":">","[":"]"}
scores = {')':3, ']':57,'}':1197,'>':25137}
for l in chunks:
  corrupted = False

  s = []
  for c in l:
    if c in needs:
      s.append(needs[c])
    else:
      if s.pop(-1) != c:
        summed+=scores[c]
        corrupted = True
        break
  if not corrupted:
    incompletes.append(s[::-1])

print(summed, median([p2s(c) for c in incompletes]))


# for line in chunks:
#   l = []
#   # print(line)
#   for c in line:
#     if c in lookup:
#       l.append(c)
#     else:
#       lastChar = "" if len(l) == 0 else l.pop()
#       #last char needs to an opening and its lookup needs to match otherwise increment
#       if lastChar in lookup and lookup[lastChar] == c:
#         pass
#       else:
#         sum_bad_closing[c]+=1
#         continue

  # print(sum_bad_closing)


     


