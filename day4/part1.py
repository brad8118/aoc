# https://adventofcode.com/2021/day/4
def calcSum(board):
  sum = 0;
  for row in board:
    for item in row:
      if item["checked"] == False:
        sum += item["number"]

  return sum


def checkRowAndColumn(board, x, y):
  #check row
  uncheckedItems = list(filter(lambda x: x["checked"] == False, board[x]))
  # print("unchecked", uncheckedItems)

  if len(uncheckedItems) == 0: return True
  
  #check column
  #loop board, select column, create list of checked state
  return not False in [row[y]["checked"] for row in board]

dataFile = "data.txt"
# dataFile = "test1.txt"
# dataFile = "test2.txt"

bingo_numbers = []
boad_size = 0

boards = []

#make martix from data
with open(dataFile) as file:
  bingo_numbers = file.readline().rstrip().split(",")
  bingo_numbers = [int(i) for i in bingo_numbers]

  file.readline()

  board = []
  keep_looping = True
  while(keep_looping):
    # print("new board")
    keep_looping = False
    board = []

    while (line := file.readline().rstrip()):
      keep_looping = True
      # print("line", line)
      #create row of objs {# , checked}
      row = []
      for num in line.split(" "):
        if num:
          row.append(
            { "checked": False,
            "number": int(num) 
            })
      board.append(row)
    
    if board: 
      boards.append(board)

  # print(boards)
for number in bingo_numbers:
  for board_index, board in enumerate(boards):
    # print("new board", number)
    for x in range(len(board)):
      for y in range(len(board)):
        # print("#", number, board[x][y])
        if board[x][y]["number"] == number:
          board[x][y]["checked"] = True
          winner = checkRowAndColumn(board, x, y)
          if winner:
            sum = calcSum(board)
            print("Sum", sum, "#", number, sum * number)
            break          

  



