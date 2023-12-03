from aoc import utils

COLORS = ["red", "green", "blue"]
LINE = "Game 79: 7 red, 1 green; 1 blue, 6 red, 2 green; 1 blue, 12 red"


def init_colors_count():
    colors_count = {}
    for color in COLORS:
        colors_count[color] = 0
    return colors_count


def game_minimum_cubes(line) -> bool:
    game_id = int(line.split(":")[0].split(" ")[1])
    game_sets = [single_set.strip() for single_set in line.split(":")[1].split(";")]

    minimum_cubes = init_colors_count()

    for game_set in game_sets:
        set_minimum_cubes = game_set_minimum_cubes(game_set)
        for cube_color in COLORS:
            if set_minimum_cubes[cube_color] > minimum_cubes[cube_color]:
                minimum_cubes[cube_color] = set_minimum_cubes[cube_color]

    return game_id, minimum_cubes


def game_set_minimum_cubes(single_set) -> tuple:
    set_cubes = [single_cube.strip() for single_cube in single_set.split(",")]
    minimum_cubes = init_colors_count()

    for set_cube in set_cubes:
        cube_color = set_cube.split(" ")[1]
        cube_quantity = int(set_cube.split(" ")[0])
        if cube_quantity > minimum_cubes[cube_color]:
            minimum_cubes[cube_color] = cube_quantity
    return minimum_cubes


def compute_game_power(game_minimum_cubes) -> int:
    game_power = 1
    for color in COLORS:
        game_power *= game_minimum_cubes[color]
    return game_power


def main(input_file="input"):
    lines = utils.read_file(input_file)
    games_power_sum = 0
    for line in lines:
        print(line)
        game_id, minimum_cubes = game_minimum_cubes(line)
        game_power = compute_game_power(minimum_cubes)
        print(f"\tMinimum cubes: {minimum_cubes}")
        print(f"\tPower: {game_power}")

        games_power_sum += game_power
    print(f"Games power sum: {games_power_sum}")
    return games_power_sum


if __name__ == "__main__":
    import sys

    main(sys.argv[1] if len(sys.argv) > 1 else None)
