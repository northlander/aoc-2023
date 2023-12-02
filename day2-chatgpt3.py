# Define the cube counts in the bag
bag_counts = {"red": 12, "green": 13, "blue": 14}

# Function to check if a game is possible
def is_possible(game, bag_counts):
    counts = bag_counts.copy()
    subsets = game.split("; ")
    for subset in subsets:
        cubes = subset.split(", ")
        for cube in cubes:
            color, count = cube.split()
            count = int(count)
            if counts[color] < count:
                return False
            counts[color] -= count
    return True

with open('day2.txt', 'r') as f:
  games = f.readlines()

  # Find possible games and calculate the sum of their IDs
  possible_games = []
  for game in games:
      game_id, revealed_cubes = game.split(": ")
      if is_possible(revealed_cubes, bag_counts):
          possible_games.append(int(game_id.split()[-1]))

  # Calculate the sum of the IDs of possible games
  result = sum(possible_games)
  print("The sum of the IDs of possible games is:", result)