import re

input = open("input.txt")
test = open("test.txt")

def ans(input):
  sum = 0
  for line in input:
    line = line.replace("one", "o1e")
    line = line.replace("two", "t2o")
    line = line.replace("three", "t3e")
    line = line.replace("four", "f4r")
    line = line.replace("five", "f5e")
    line = line.replace("six", "s6x")
    line = line.replace("seven", "s7n")
    line = line.replace("eight", "e8t")
    line = line.replace("nine", "n9e")
    firstDigit, lastDigit = findFirstAndLastNumber(line)
    firstDigit, lastDigit = str(firstDigit), str(lastDigit)
    num = int(firstDigit + lastDigit)
    sum += num
    print(firstDigit + "+" + lastDigit + "=" + str(num) + ",     " + line)
  return sum

def findFirstAndLastNumber(string):
  word_to_num = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
  
  for word, num in word_to_num.items():
    string = string.replace(word, str(num))
  numbers = re.findall(r'\d', string)
  if numbers:
    return numbers[0], numbers[-1]
  return None, None


print(ans(input))
