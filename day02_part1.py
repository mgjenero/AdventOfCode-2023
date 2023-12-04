limitations = {
    "green": 13,
    "red": 12,
    "blue": 14}


def parse_game(game: str):
    game_id, cubes = game.split(":")
    game_id = game_id.split(" ")[1]
    cubes = cubes.split(";")
    cubes = [cube.strip() for cube in cubes]
    return game_id, cubes


def is_possible_game(cubes: str, limitations: dict) -> bool:
    for cube_grab in cubes:
        cube_grab = cube_grab.split(",")
        cube_grab = [cube.strip() for cube in cube_grab]
        for cube in cube_grab:
            number, color = cube.split(" ")
            if int(number) > limitations[color]:
                return False
    return True


def sum_possible_games(games, limitations):
    sum = 0
    for game in games:
        game_id, cubes = parse_game(game)
        if is_possible_game(cubes, limitations):
            sum += int(game_id)
    return sum


# Testing
test1 = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]
ans1 = 8

assert sum_possible_games(test1, limitations) == ans1

# Read input
with open("day2.txt", "r") as f:
    lines = f.readlines()
    print(sum_possible_games(lines, limitations))

# Runtime = O(n * m)
# Space O(1)
#
# where n is number of games
# m is the maximum number of cube grabs in a game.
