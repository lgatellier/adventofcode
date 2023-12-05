from __future__ import annotations

from aoc import utils


class Range:
    def __init__(self, start: int, end: int = None, length: int = None) -> None:
        self.start = start
        if length:
            self.end = start + length - 1
        elif end:
            self.end = end
        else:
            self.end = start

    @property
    def length(self) -> int:
        return self.end - self.start + 1

    def overlaps(self, __r: Range) -> bool:
        if __r.end < self.start:
            return False
        if __r.start > self.end:
            return False
        return True

    def __and__(self, __r: Range) -> Range:
        if not self.overlaps(__r):
            return None
        return Range(max(self.start, __r.start), min(self.end, __r.end))

    def __eq__(self, __value: object) -> bool:
        return (
            isinstance(__value, Range)
            and self.start == __value.start
            and self.end == __value.end
        )

    def __repr__(self) -> str:
        return f"Range({self.start},{self.end})"


class Mapping:
    def __init__(self, dest_start: int, src_start: int, length: int):
        self.src = Range(src_start, src_start + length - 1)
        self.dest = Range(dest_start, dest_start + length - 1)
        self.length = length

    def matches(self, __r: Range):
        return self.src.overlaps(__r)

    def map(self, value: int):
        return self.dest.start + value - self.src.start

    def map_range(self, __r: Range):
        if __r.start < self.src.start or __r.end > self.src.end:
            raise ValueError(
                "Cannot map a range which is not included inside mapping src boundaries"
            )
        start_delta = __r.start - self.src.start
        end_delta = self.src.end - __r.end
        return Range(self.dest.start + start_delta, self.dest.end - end_delta)

    def __repr__(self) -> str:
        return f"Mapping[src={self.src}, dest={self.dest}]"

    @staticmethod
    def parse(line: str) -> Mapping:
        split = line.split(" ")
        return Mapping(int(split[0]), int(split[1]), int(split[2]))


class Context:
    def __init__(self, seeds: list[int] = None, seed_ranges: list[Range] = None):
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
            self.__maps[map] + [mapping], key=lambda m: m.src.start
        )

    def map_value(self, map: str, src: int) -> int:
        utils.verbose("Looking for mapping of type {type}", type=map)
        if map not in self.__maps:
            raise ValueError(f"Non existing map {map}")
        mapping = self.__find_least_or_equal_mapping(map, Range(src))
        utils.verbose("Potentially matching mapping : {mapping}", mapping=mapping)
        dest_value = mapping.map(src) if mapping else src
        utils.verbose(
            "Mapping : {map} : {src_value} => {dest_value}",
            map=map,
            src_value=src,
            dest_value=dest_value,
        )
        return dest_value

    def map_range(self, map: str, src: Range) -> list[Range]:
        mapping = self.__find_least_or_equal_mapping(map, Range(src.start, src.start))
        if not mapping:
            utils.verbose("No mapping found")
            return [src]

        utils.verbose("Found matching mapping {mapping}", mapping=mapping)
        matching_range = src & mapping.src
        result: list[Range] = []
        if matching_range.start > src.start:
            result.append(Range(src.start, matching_range.start - 1))
        result.append(mapping.map_range(matching_range))
        if matching_range.end < src.end:
            for __r in self.map_range(map, Range(matching_range.end + 1, src.end)):
                result.append(__r)
        return result

    def __find_least_or_equal_mapping(self, map: str, src: Range) -> Mapping:
        utils.verbose(
            "Looking for mapping of type {map} corresponding to value {value}",
            map=map,
            value=src,
        )
        last_value = None
        for mapping in self.__maps[map]:
            if mapping.matches(src):
                last_value = mapping
                utils.verbose("Found matching mapping {mapping}", mapping=mapping)
        return last_value


def parse_context(lines: list[str], ranges: bool = False) -> Context:
    seed_values = [int(seed) for seed in lines[0].split(" ")[1:]]
    if ranges:
        seed_ranges = sorted(
            [
                Range(seed_values[i], length=seed_values[i + 1])
                for i in range(0, len(seed_values), 2)
            ],
            key=lambda r: r.start,
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
