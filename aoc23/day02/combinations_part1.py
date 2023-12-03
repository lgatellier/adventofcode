CUBES = {"red": 12, "green": 13, "blue": 14}

LINE = "Game 79: 7 red, 1 green; 1 blue, 6 red, 2 green; 1 blue, 12 red"


def read_file(input):
    with open(input, "r") as f:
        return [line.strip() for line in f.readlines()]


def is_game_possible(line) -> bool:
    game_id = int(line.split(":")[0].split(" ")[1])
    game_sets = [single_set.strip() for single_set in line.split(":")[1].split(";")]
    for game_set in game_sets:
        if is_set_possible(game_set):
            print(f"Set {game_set} is possible")
        else:
            return game_id, False
    print(f"Game {game_id} is possible")
    return game_id, True


def is_set_possible(set) -> bool:
    set_cubes = [single_cube.strip() for single_cube in set.split(",")]
    for set_cube in set_cubes:
        cube_color = set_cube.split(" ")[1]
        cube_quantity = int(set_cube.split(" ")[0])
        if cube_quantity > CUBES[cube_color]:
            return False
    return True


def main():
    input = "input"
    lines = read_file(input)
    possible_games = []
    for line in lines:
        game_id, possible = is_game_possible(line)
        if possible:
            possible_games.append(game_id)
    print(f"Possible games: {possible_games}")
    print(sum(possible_games))


main()
