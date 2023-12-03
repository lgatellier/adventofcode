from aoc import utils


CUBES = {"red": 12, "green": 13, "blue": 14}


def is_game_possible(line) -> bool:
    game_id = int(line.split(":")[0].split(" ")[1])
    game_sets = [single_set.strip() for single_set in line.split(":")[1].split(";")]
    for game_set in game_sets:
        if is_set_possible(game_set):
            utils.verbose(f"Set {game_set} is possible")
        else:
            return game_id, False
    utils.verbose(f"Game {game_id} is possible")
    return game_id, True


def is_set_possible(set) -> bool:
    set_cubes = [single_cube.strip() for single_cube in set.split(",")]
    for set_cube in set_cubes:
        cube_color = set_cube.split(" ")[1]
        cube_quantity = int(set_cube.split(" ")[0])
        if cube_quantity > CUBES[cube_color]:
            return False
    return True


def main(input_file="input"):
    lines = utils.read_file(input_file)
    possible_games = []
    for line in lines:
        game_id, possible = is_game_possible(line)
        if possible:
            possible_games.append(game_id)

    print(f"Possible games found : {possible_games}")
    possible_games_sum = sum(possible_games)
    print(f"Sum of possible games is {possible_games_sum}")
    return possible_games_sum


if __name__ == "__main__":
    utils.main(main)
