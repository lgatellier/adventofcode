from aoc import utils
from aoc.y22.day05 import Crates, Move


def test_crates_parsing():
    utils.state["verbose"] = True
    lines = ["[P]     [L] [T]", "[L] [M] [G] [G]", " 1   2   3   4 "]
    stacks = Crates.parse(lines).stacks
    assert len(stacks) == 4
    assert stacks[0].pop() == "P"
    assert stacks[0].pop() == "L"
    assert stacks[1].pop() == "M"
    assert stacks[2].pop() == "L"
    assert stacks[2].pop() == "G"
    assert stacks[3].pop() == "T"
    assert stacks[3].pop() == "G"


def test_move_parsing():
    move = Move.parse("move 9 from 5 to 1")
    assert move.nb_to_move == 9
    assert move.from_stack == 4
    assert move.to_stack == 0


def test_apply_move():
    lines = ["[P]     [L] [T]", "[L] [M] [G] [G]", " 1   2   3   4 "]
    crates = Crates.parse(lines)
    assert len(crates.stacks[0]) == 2
    crates.apply_move(Move(2, 0, 1))
    assert len(crates.stacks[0]) == 0
