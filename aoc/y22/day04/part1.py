from aoc.y22.day04 import PairOfElves


def main(lines: list[str]):
    pairs = [PairOfElves.parse(line) for line in lines]
    fully_overlapping_pairs = [pair for pair in pairs if pair.fully_overlap]
    fully_overlapping_pairs_count = len(fully_overlapping_pairs)
    print(f"{fully_overlapping_pairs_count} pairs fully overlap")
    return fully_overlapping_pairs_count
