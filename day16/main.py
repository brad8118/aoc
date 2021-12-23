# https://adventofcode.com/2021/day/16

# from collections import Counter
# from datetime import datetime, timedelta
# import queue
import math

class Packet:
  def __init__(self,version,typeId):
    self.version = version
    self.typeId = typeId
    self.literal = None
    self.packets = []
  
  def __repr__(self):
    return "P: v:{} t:{} l:{} []:{}".format(self.version, self.typeId, self.literal,  self.packets)

  def __str__(self):
    return "P: v:{} t:{} l:{} p[]:{}".format(self.version, self.typeId, self.literal,  self.packets)

class AOC_2021_day16:
  def __init__(self):
    self.packets = []
    self.bin_input=""
    self.index=0
    self.hex_input = ""

  def remainingBits(self):
    return self.bin_input[self.index:]

  def printRemainingBits(self):
    print(self.remainingBits())

  def readFile(self, file):
    with open(file) as file:
      while (line := file.readline().rstrip()):
        self.hex_input = line
        self.bin_input = (bin(int(line, 16))[2:]).zfill(len(line)*4)

  def nextBits(self, n):
    if n+ self.index > len(self.bin_input):
      raise Exception("Yikes not enough left","n", n, "i", self.index, self.remainingBits())

    bits = self.bin_input[self.index: self.index+n]
    self.index +=n
    # print(bits, "len", len(bits), "base2", int(bits,2))
    return bits

  def calcValue(self, typeId, packets):
    value = 0
    if typeId == 0: #sum
      value = sum([p.literal for p in packets])
    elif typeId == 1: #product ++
      value = math.prod([p.literal for p in packets])
    elif typeId == 2: #minimum 
      value = min([p.literal for p in packets])
    elif typeId == 3: #max 
      value = max([p.literal for p in packets])
    elif typeId == 4: #max 
      raise Exception("Shouldn't be here")
    elif typeId == 5: #greater than 
      value = 1 if packets[0].literal > packets[1].literal else 0
    elif typeId == 6: #less than 
      value = 1 if packets[0].literal < packets[1].literal else 0
    elif typeId ==7: #equal to than 
      value = 1 if packets[0].literal == packets[1].literal else 0
    else: #less than 
      raise Exception("Shouldn't be here, invalid #", typeId)

    return value

  def createPacket(self):
    version = self.nextBits(3)
    typeId = self.nextBits(3)
    packet = Packet(int(version,2), int(typeId,2))  
    self.packets.append(packet)

    if packet.typeId == 4:
      packet.literal = self.parseLiteral()
    else:
      packets = self.parseOperator()
      packet.packets.extend(packets)
      packet.literal = self.calcValue(packet.typeId, packets)

    return packet

  # def createSubpacket(self, lengthOfPacket):

  def parseLiteral(self):
    found_leading_zero = False
    binNum = ""
    while(not found_leading_zero):
      bits = self.nextBits(5)
      binNum += bits[1:5]
      found_leading_zero = bits[0] == "0"
    return int(binNum,2)

  def parseOperator(self):
    packets=[]
    lengthTypeID = self.nextBits(1)
    lenghtInBitOfSubPackets, numberSubPacketsContained = None, None
    if lengthTypeID == "0": #use 15 bits
      lenghtInBitsOfSubPackets = int(self.nextBits(15),2)
      startingIndex = self.index      
      while lenghtInBitsOfSubPackets != self.index-startingIndex:
        packets.append(self.createPacket())
        diff = self.index-startingIndex
    elif lengthTypeID == "1": #use 11 bits
      numberSubPacketsContained = int(self.nextBits(11),2)
      for i in range(numberSubPacketsContained):
        packets.append(self.createPacket())

    return packets

  def part1(self):
    # print(self.hex_input)
    # self.printRemainingBits()
    packet = self.createPacket()
    # print(self.packets)
    # print("packet-packets", packet.packets)
    total = sum([p.version for p in self.packets])
    print("Part1", "packets", len(self.packets), "total", total)
    # print("Part2", packet.literal)

  def part2(self):
    print("Part2", self.packets[0].literal)
    

dataFile = "data.txt"
# dataFile = "test1.txt"
# dataFile = "test2.txt"

aoc = AOC_2021_day16()
aoc.readFile(dataFile)
aoc.part1()
aoc.part2()