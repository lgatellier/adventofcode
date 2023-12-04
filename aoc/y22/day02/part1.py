from aoc.y22.day02 import parse_rounds, Round


class Part1Round(Round):
    def __init__(self, opponent_choice, self_choice):
        super().__init__(opponent_choice)
        self._self_choice = self_choice


def main(lines: list[str]):
    rounds = parse_rounds(lines, Part1Round)
    print(f"Total score : {sum(r.score() for r in rounds)}")
    return sum(r.score() for r in rounds)
