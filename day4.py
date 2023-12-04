def day4_1():
  result = 0
  with open('day4.txt', 'r') as f:
    lines = f.readlines()
    for y, line in enumerate(lines):
      _, game = line.split(':')
      winning_part, my_part = game.split(' |')
      winning_nums = [int(n) for n in winning_part.split()]
      my_nums = [int(n) for n in my_part.split()]
      score = 0
      for idx, num in enumerate(my_nums):
        if num in winning_nums:
          score = max(score * 2, 1)
      result += score
  print(result)


def day4_2():
  result = 0
  cards = dict()
  with open('day4.txt', 'r') as f:
    lines = f.readlines()
    for y, line in enumerate(lines):
      _, game = line.split(':')
      winning_part, my_part = game.split(' |')
      winning_nums = [int(n) for n in winning_part.split()]
      cards[y+1] = len([int(n) for n in my_part.split() if int(n) in winning_nums])

  num_cards = {s: 1 for s in range(1, len(cards)+1)}
  for i in range(1, len(cards)+1):
    result += num_cards[i]
    for x in range(i+1, i+cards[i]+1):
      num_cards[x] += num_cards[i]
  print(result)


day4_1()
day4_2()
