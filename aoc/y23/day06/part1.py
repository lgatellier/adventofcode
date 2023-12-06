from aoc.y23.day06 import parse_races, parse_records, parse_times


def main(lines: list[str]):
    times = parse_times(lines[0])
    records = parse_records(lines[1])
    races = parse_races(times, records)

    numbers_of_ways_to_win = [r.number_of_ways_to_win() for r in races]
    number_of_ways_to_win_multiplied = 1
    for number_of_ways_to_win in numbers_of_ways_to_win:
        number_of_ways_to_win_multiplied = (
            number_of_ways_to_win_multiplied * number_of_ways_to_win
        )
    print(f"Numbers of ways to win : {numbers_of_ways_to_win}")
    print(f"Multiplied cound : {number_of_ways_to_win_multiplied}")
    return number_of_ways_to_win_multiplied
