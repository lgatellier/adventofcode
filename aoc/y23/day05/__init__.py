from collections import OrderedDict

from aoc import utils


class Context:
    def __init__(self, seeds: list[int]):
        self.seeds = seeds
        self.__maps = {
            "seed": {},
            "soil": {},
            "fertilizer": {},
            "water": {},
            "light": {},
            "temperature": {},
            "humidity": {},
        }

    def add_mapping(
        self, map: str, dest_start: int, src_start: int, range_length: int
    ) -> None:
        if map not in self.__maps:
            raise ValueError(f"Non existing map {map}")
        utils.verbose(
            "Adding mapping {map}, dest={dest}, src={src}, length={length}",
            map=map,
            dest=dest_start,
            src=src_start,
            length=range_length,
        )
        self.__maps[map][src_start] = {
            "src_start": src_start,
            "dest_start": dest_start,
            "length": range_length,
        }

    def sort_mappings(self):
        for map in self.__maps.keys():
            self.__maps[map] = OrderedDict(sorted(self.__maps[map].items()))

    def map_value(self, map: str, searched_value: int) -> int:
        utils.verbose("Looking for mapping of type {type}", type=map)
        if map not in self.__maps:
            raise ValueError(f"Non existing map {map}")
        mapping = self.__find_least_or_equal_mapping(map, searched_value)
        utils.verbose("Potentially matching mapping : {mapping}", mapping=mapping)
        print(mapping)
        print(searched_value)
        if (
            mapping
            and mapping["src_start"]
            <= searched_value
            <= mapping["src_start"] + mapping["length"]
        ):
            dest_value = mapping["dest_start"] + (searched_value - mapping["src_start"])
        else:
            dest_value = searched_value
        utils.verbose(
            "Mapping : {map} : {src_value} => {dest_value}",
            map=map,
            src_value=searched_value,
            dest_value=dest_value,
        )
        return dest_value

    def __find_least_or_equal_mapping(self, map: str, searched_value: int) -> dict:
        utils.verbose(
            "Looking for mapping of type {map} corresponding to value {value}",
            map=map,
            value=searched_value,
        )
        last_value = None
        for key, value in self.__maps[map].items():
            if key <= searched_value:
                utils.verbose(
                    "Found mapping for key={key} : {value}", key=key, value=value
                )
                last_value = value
        return last_value


def parse_context(lines: list[str]) -> Context:
    ctx = Context([int(seed) for seed in lines[0].split(" ")[1:]])

    current_mapping: str = None
    for line in lines[1:]:
        if line == "":
            continue
        elif line[-4:] == "map:":
            current_mapping = line.split("-")[0]
        else:
            split = line.split(" ")
            ctx.add_mapping(
                current_mapping, int(split[0]), int(split[1]), int(split[2])
            )
    ctx.sort_mappings()
    return ctx
