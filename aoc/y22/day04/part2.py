from aoc.y22.day04 import PairOfElves


def main(lines: list[str]):
    pairs = [PairOfElves.parse(line) for line in lines]
    partially_overlapping_pairs = [pair for pair in pairs if pair.partially_overlap]
    partially_overlapping_pairs_count = len(partially_overlapping_pairs)
    print(f"{partially_overlapping_pairs_count} pairs partially overlap")
    return partially_overlapping_pairs_count
