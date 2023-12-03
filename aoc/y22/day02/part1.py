from aoc import utils
from aoc.y22.day02 import parse_rounds, Round


class Part1Round(Round):
    def __init__(self, opponent_choice, self_choice):
        super().__init__(opponent_choice)
        self._self_choice = self_choice


def main(input_file="input"):
    lines = utils.read_file(input_file)
    rounds = parse_rounds(lines, Part1Round)
    print(f"Total score : {sum(r.score() for r in rounds)}")
    return sum(r.score() for r in rounds)
