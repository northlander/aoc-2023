def day2_1():
  result = 0
  with open('day2.txt', 'r') as f:
    lines = f.readlines()

    for line in lines:
      game_num_part, game_part = line.split(':')
      game_num = int(game_num_part[5:])
      sets = game_part.split(';')
      max_cubes = {'blue': 0, 'green': 0, 'red': 0}
      for s in sets:
        cubes = s.split(',')
        for cube in cubes:
          num, color = cube.strip().split(' ')
          max_cubes[color] = max(max_cubes[color], int(num))

      if max_cubes['red'] <= 12 and max_cubes['green'] <= 13 and max_cubes['blue'] <= 14:
        result += game_num

  print(result)

def day2_2():
  result = 0
  with open('day2.txt', 'r') as f:
    lines = f.readlines()

    for line in lines:
      game_num_part, game_part = line.split(':')
      game_num = int(game_num_part[5:])
      sets = game_part.split(';')
      max_cubes = {'blue': 0, 'green': 0, 'red': 0}
      for s in sets:
        cubes = s.split(',')
        for cube in cubes:
          num, color = cube.strip().split(' ')
          max_cubes[color] = max(max_cubes[color], int(num))
      power = max_cubes['blue']*max_cubes['green']*max_cubes['red']
      result += power
  print(result)

day2_1()
day2_2()