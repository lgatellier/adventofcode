from __future__ import annotations

from aoc import utils


class Race:
    def __init__(self, duration: int, record: int):
        self.duration = duration
        self.record = record

    def is_winning_choice(self, hold_duration: int):
        speed = hold_duration  # speed is <hold_duration> mm/ms
        move_duration = self.duration - hold_duration
        distance = speed * move_duration
        utils.verbose(
            "With a speed of {speed}, you'll move during {move_duration} ms and gone {distance} mm",
            speed=speed,
            move_duration=move_duration,
            distance=distance,
        )
        return distance > self.record

    def number_of_ways_to_win(self):
        ways_to_win = []
        utils.verbose(
            "Finding ways to win a race of {duration} ms with a record of {record} mm",
            duration=self.duration,
            record=self.record,
        )
        min_to_win = None
        max_to_win = None
        i = 0
        while not min_to_win or not max_to_win:
            # i is the numebr of ms you hold the button
            if self.is_winning_choice(i):
                utils.verbose("Holding the button {i} ms is a winning choice", i=i)
                min_to_win = i
            if self.is_winning_choice(self.duration - i):
                utils.verbose(
                    "Holding the button {i} ms is a winning choice", i=self.duration - i
                )
                max_to_win = self.duration - i
            if (
                i + 25000 <= self.duration
                and not self.is_winning_choice(i + 25000)
                and not self.is_winning_choice(self.duration - i - 25000)
            ):
                i += 25000
            else:
                i += 1

        utils.verbose(
            "Found {number_wtw} ways to win the race {race}",
            number_wtw=len(ways_to_win),
            race=self,
        )
        return max_to_win - min_to_win + 1

    def __repr__(self) -> str:
        return f"Race[{self.duration},{self.record}]"


def parse_records(line: str, joint=False) -> list[int]:
    str_records = [t for t in line[9:].split(" ") if t != ""]
    if joint:
        str_records = ["".join(str_records)]
    return list(map(int, str_records))


def parse_times(line: str, joint=False) -> list[int]:
    str_times = [t for t in line[5:].split(" ") if t != ""]
    if joint:
        str_times = ["".join(str_times)]
    return list(map(int, str_times))


def parse_races(times: list[int], records: list[int]):
    races: list[Race] = []
    for i in range(len(times)):
        races.append(Race(times[i], records[i]))
    print(f"Races found : {races}")
    return races
