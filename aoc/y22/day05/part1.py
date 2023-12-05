from aoc.y22.day05 import Crates, Move


def main(lines: list[str]):
    crates = None
    i = 0
    while not crates:
        # empty line is delimiter between initial crates positions and moves list
        if lines[i] == "":
            crates = Crates.parse(lines[0:i])
        i += 1
    for j in range(i, len(lines)):
        move = Move.parse(lines[j])
        crates.apply_move(move)

    sequence = [stack.pop() for stack in crates.stacks if len(stack) > 0]
    print(sequence)
