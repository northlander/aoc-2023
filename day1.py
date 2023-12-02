def day1():
  sum = 0
  with open('day1.txt', 'r') as f:
    data = f.read().splitlines()
    for line in data:
      first = 0
      last = 0
      for c in line:
        if c.isnumeric():
          first = c
          break
         
      for c in reversed(line):
        if c.isnumeric():
          last = c
          break
      sum += int(first+last)
  print(sum)

text_nums = {'one': '1', 'two': '2', 'three': '3', 'four': '4','five': '5','six':'6','seven':'7','eight': '8','nine':'9'}

def day1_2():
  sum_result = 0
  with open('day1.txt', 'r') as f:
    data = f.read().splitlines()
    for line in data:
      first = first_num(line)    
      last = last_num(line)
      sum_result += int(first+last)
  print(sum_result)

def first_num(str):
  if str[0].isnumeric():
    return str[0]
  for key, value in text_nums.items():
    if str.startswith(key):
      return value
  return first_num(str[1:])

def last_num(str):
  if str[-1].isnumeric():
    return str[-1]
  for key, value in text_nums.items():
    if str.endswith(key):
      return value
  return last_num(str[:-1])

day1()
day1_2()
