from __future__ import annotations

from aoc import utils


class Mapping:
    def __init__(self, dest_start: int, src_start: int, range_length: int):
        self.__src_start = src_start
        self.__src_end = src_start + range_length - 1
        self.__dest_start = dest_start
        self.__dest_end = dest_start + range_length - 1
        self.__range_length = range_length

    def matches(self, value: int):
        return self.__src_start <= value <= self.__src_end

    def map(self, value: int):
        return self.__dest_start + value - self.__src_start

    @property
    def src_start(self):
        return self.__src_start

    def __repr__(self) -> str:
        return f"Mapping[src_start={self.src_start}, src_end={self.__src_end}, dest_start={self.__dest_start}]"

    @staticmethod
    def parse(line: str) -> Mapping:
        split = line.split(" ")
        return Mapping(int(split[0]), int(split[1]), int(split[2]))


class Context:
    def __init__(self, seeds: list[int] = None, seed_ranges: list[tuple[int]] = None):
        self.seeds = seeds
        self.seed_ranges = seed_ranges
        self.__maps: dict[str, list[Mapping]] = {
            "seed": [],
            "soil": [],
            "fertilizer": [],
            "water": [],
            "light": [],
            "temperature": [],
            "humidity": [],
        }

    def add_mapping(self, map: str, mapping: Mapping) -> None:
        if map not in self.__maps:
            raise ValueError(f"Non existing map {map}")
        utils.verbose("Adding {map} mapping : {mapping}", map=map, mapping=mapping)
        self.__maps[map] = sorted(
            self.__maps[map] + [mapping], key=lambda m: m.src_start
        )

    def map_value(self, map: str, searched_value: int) -> int:
        utils.verbose("Looking for mapping of type {type}", type=map)
        if map not in self.__maps:
            raise ValueError(f"Non existing map {map}")
        mapping = self.__find_least_or_equal_mapping(map, searched_value)
        utils.verbose("Potentially matching mapping : {mapping}", mapping=mapping)
        dest_value = mapping.map(searched_value) if mapping else searched_value
        utils.verbose(
            "Mapping : {map} : {src_value} => {dest_value}",
            map=map,
            src_value=searched_value,
            dest_value=dest_value,
        )
        return dest_value

    def __find_least_or_equal_mapping(self, map: str, searched_value: int) -> Mapping:
        utils.verbose(
            "Looking for mapping of type {map} corresponding to value {value}",
            map=map,
            value=searched_value,
        )
        last_value = None
        for mapping in self.__maps[map]:
            if mapping.matches(searched_value):
                last_value = mapping
                utils.verbose("Found matching mapping {mapping}", mapping=mapping)
        return last_value


def parse_context(lines: list[str], ranges: bool = False) -> Context:
    seed_values = [int(seed) for seed in lines[0].split(" ")[1:]]
    if ranges:
        seed_ranges = sorted(
            [
                (seed_values[i], seed_values[i + 1])
                for i in range(0, len(seed_values), 2)
            ],
            key=lambda r: r[0],
        )
        ctx = Context(seed_ranges=seed_ranges)
    else:
        ctx = Context(seeds=seed_values)

    current_mapping: str = None
    for line in lines[1:]:
        if line == "":
            continue
        elif line[-4:] == "map:":
            current_mapping = line.split("-")[0]
        else:
            mapping = Mapping.parse(line)
            ctx.add_mapping(current_mapping, mapping)
    return ctx
