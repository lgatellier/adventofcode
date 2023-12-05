from __future__ import annotations
import copy


from aoc import utils


class Stack:
    def __init__(self):
        self._stack: list[str] = []

    def append(self, item: str):
        self._stack.append(item)

    def pop(self) -> str:
        return self._stack.pop()

    def __len__(self):
        return len(self._stack)


class Crates:
    def __init__(self, stack_count: int):
        self._stacks = [Stack() for i in range(stack_count)]
        utils.verbose("Initializing Crates with {n} stacks", n=len(self._stacks))

    @property
    def stacks(self) -> list[Stack]:
        return [copy.copy(stack) for stack in self._stacks]

    def apply_move(self, move: Move):
        utils.verbose(
            "Moving {n} crates from stack {a} to stack {b}",
            n=move.nb_to_move,
            a=move.from_stack,
            b=move.to_stack,
        )
        for i in range(0, move.nb_to_move):
            crate_to_move = self._stacks[move.from_stack].pop()
            utils.verbose("Moving {c}", c=crate_to_move)
            self._stacks[move.to_stack].append(crate_to_move)

    def __stack_append(self, stack_index: int, item: str) -> None:
        utils.verbose("Pushing item {item} to stack {s}", item=item, s=stack_index)
        self._stacks[stack_index].append(item)
        utils.verbose(
            "Stack {stack} size is now {size}",
            stack=stack_index,
            size=len(self._stacks[stack_index]),
        )

    @staticmethod
    def parse(lines: list[str]) -> Crates:
        last_line = lines[len(lines) - 1]
        stack_count = (len(last_line) + 1) // 4
        crates = Crates(stack_count)
        for y in range(len(lines) - 2, -1, -1):
            line = lines[y]
            utils.verbose("Processing line {y}", y=y)
            for x in range(0, len(line), 4):
                stack_index = x // 4
                if line[x + 1] != " ":
                    crates.__stack_append(stack_index, line[x + 1])
        return crates


class Move:
    def __init__(self, nb_to_move: int, from_stack: int, to_stack: int):
        self.nb_to_move = nb_to_move
        self.from_stack = from_stack
        self.to_stack = to_stack

    @staticmethod
    def parse(line) -> Move:
        split = line.split(" ")
        return Move(int(split[1]), int(split[3]) - 1, int(split[5]) - 1)
