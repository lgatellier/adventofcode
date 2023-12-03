from aoc import utils
from aoc.y22.day02 import parse_rounds, Round


class Part2Round(Round):
    SHAPE_TO_PLAY = {
        "A": {  # rock
            "X": "Z",  # loose
            "Y": "X",  # draw
            "Z": "Y",  # win
        },
        "B": {  # paper
            "X": "X",  # loose
            "Y": "Y",  # draw
            "Z": "Z",  # win
        },
        "C": {  # scissors
            "X": "Y",  # loose
            "Y": "Z",  # draw
            "Z": "X",  # win
        },
    }

    def __init__(self, opponent_choice, round_result):
        super().__init__(opponent_choice)
        self._self_choice = self.SHAPE_TO_PLAY[self._opponent_choice][round_result]


def main(input_file="input"):
    lines = utils.read_file(input_file)
    rounds = parse_rounds(lines, Part2Round)
    print(f"Total score : {sum(r.score() for r in rounds)}")
    return sum(r.score() for r in rounds)
