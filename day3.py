from collections import namedtuple

Symbol = namedtuple('Symbol', ['x','y','type'])
Part = namedtuple('Part', ['y','xstart','xend','value'])

def parse():
  symbols = []
  parts = []
  with open('day3.txt', 'r') as f:
    lines = f.readlines()
    current_num = ''
    for y, line in enumerate(lines):
      for x, c in enumerate(line):
        if c == '.' or c == '\n': 
          if len(current_num) > 0:
            parts.append(Part(y, x-len(current_num), x-1, int(current_num)))
            current_num = ''
          continue
        if not c.isnumeric():
          symbols.append(Symbol(x, y, c))
          if len(current_num) > 0:
            parts.append(Part(y, x-len(current_num), x-1, int(current_num)))
            current_num = ''
        else:
          current_num += c
  return (symbols, parts)

def day3_1():
  result = 0
  (symbols, parts) = parse()
  for p in parts:
    matches = [s for s in symbols if s.y >= p.y-1 and s.y <= p.y+1 and s.x >= p.xstart-1 and s.x <= p.xend+1]
    if len(matches) > 0:
      result += p.value
         
  return result

def day3_2():
  result = 0
  (symbols, parts) = parse()
  for s in symbols:
    if s.type == '*':
      matches = [p for p in parts if s.y >= p.y-1 and s.y <= p.y+1 and s.x >= p.xstart-1 and s.x <= p.xend+1]
      if len(matches) == 2:
        result += matches[0].value * matches[1].value
         
  return result

print(day3_1())
print(day3_2())