from aoc.y23.day06 import parse_races, parse_records, parse_times


def main(lines: list[str]):
    times = parse_times(lines[0], joint=True)
    records = parse_records(lines[1], joint=True)
    races = parse_races(times, records)

    number_of_ways_to_win = races[0].number_of_ways_to_win()
    print(f"Numbers of ways to win : {number_of_ways_to_win}")
    return number_of_ways_to_win
