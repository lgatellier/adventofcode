from aoc import utils
from aoc.y22.day02 import parse_rounds


def main(input_file="input"):
    lines = utils.read_file(input_file)
    rounds = parse_rounds(lines)
    print(f"Total score : {sum(r.score() for r in rounds)}")
    return sum(r.score() for r in rounds)
