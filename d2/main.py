import re

input = open("input.txt")
test = open("test.txt")

# Part 1
def p1(input):
  sum = 0
  maxRed, maxGreen, maxBlue = 12, 13, 14
  for line in input:
    items = line.split(":")
    gameID = int(re.findall(r'\d+', items[0])[0])
    rounds = items[1].split(";")
    possible = True;

    for round in rounds:
      cubes = round.split(",")
      

      for cube in cubes:
        n = int(re.findall(r'\d+', cube)[0])
        if 'red' in cube:
          if n > maxRed:
            possible = False
        elif 'green' in cube:
          if n > maxGreen:
            possible = False
        elif 'blue' in cube:
          if n > maxBlue:
            possible = False

    if possible:
      sum += gameID

  return sum

# print(p1(input))

# Part 2

def p2(input):
  sum = 0
  for line in input:
    items = line.split(":")
    gameID = int(re.findall(r'\d+', items[0])[0])
    rounds = items[1].split(";")
    minRed, minGreen, minBlue = 0, 0, 0

    for round in rounds:
      cubes = round.split(",")

      for cube in cubes:
        n = int(re.findall(r'\d+', cube)[0])
        if 'red' in cube:
          minRed = max(minRed, n)

        elif 'green' in cube:
          minGreen = max(minGreen, n)

        elif 'blue' in cube:
          minBlue = max(minBlue, n)

    power = minRed * minGreen * minBlue
    sum += power

    print("Red: " + str(minRed) + " Green: " + str(minGreen) + " Blue: " + str(minBlue))

  return sum

print(p2(input))