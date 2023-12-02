def parse_game_data(game_data):
    """
    Parse the game data from the given string and return it as a list of tuples.
    Each tuple contains the game ID and a list of dictionaries, each representing a set of revealed cubes.
    """
    games = []
    for line in game_data.strip().split('\n'):
        game_id, cubes = line.split(': ')
        game_id = int(game_id.split(' ')[1])  # Extract the numerical ID
        cube_sets = cubes.split('; ')
        cube_info = []
        for cube_set in cube_sets:
            cube_counts = {}
            for cube in cube_set.split(', '):
                count, color = cube.split(' ')
                cube_counts[color] = int(count)
            cube_info.append(cube_counts)
        games.append((game_id, cube_info))
    return games

def is_game_possible(cube_sets, available_cubes):
    """
    Check if a game is possible given the available cubes.
    """
    for set in cube_sets:
        for color, count in set.items():
            if count > available_cubes[color]:
                return False
    return True

def sum_possible_game_ids(game_data):
    """
    Determine which games are possible and return the sum of their IDs.
    """
    games = parse_game_data(game_data)
    available_cubes = {'red': 12, 'green': 13, 'blue': 14}
    sum_ids = 0

    for game_id, cube_sets in games:
        if is_game_possible(cube_sets, available_cubes):
            sum_ids += game_id

    return sum_ids


def find_minimum_cubes_per_game(game_data):
    """
    Find the minimum number of cubes of each color that could have been in the bag for each game.
    """
    games = parse_game_data(game_data)
    minimum_cubes = {}

    for game_id, cube_sets in games:
        max_cubes = {'red': 0, 'green': 0, 'blue': 0}
        for set in cube_sets:
            for color in max_cubes.keys():
                max_cubes[color] = max(max_cubes[color], set.get(color, 0))
        minimum_cubes[game_id] = max_cubes

    return minimum_cubes

def calculate_power_of_cubes(cubes):
    """
    Calculate the power of a set of cubes as the product of the number of red, green, and blue cubes.
    """
    return cubes['red'] * cubes['green'] * cubes['blue']

def sum_of_powers(game_data):
    """
    Calculate the sum of the power of the minimum sets of cubes for each game.
    """
    minimum_cubes = find_minimum_cubes_per_game(game_data)
    total_power = 0

    for game_id, cubes in minimum_cubes.items():
        total_power += calculate_power_of_cubes(cubes)

    return total_power


# Sample game data
with open('day2.txt', 'r') as f:  
  game_data=f.read()

  # Calculate the sum of the IDs of possible games
  print(sum_possible_game_ids(game_data))

  # Calculate the sum of the powers of the minimum sets of cubes
  print(sum_of_powers(game_data))