from aoc.y23.day05 import parse_context, Range


def main(lines: list[str]):
    ctx = parse_context(lines, ranges=True)
    keys = [
        "seed",
        "soil",
        "fertilizer",
        "water",
        "light",
        "temperature",
        "humidity",
        "location",
    ]
    mapped_data: dict[str, list[Range]] = {
        "seed": ctx.seed_ranges,
        "soil": [],
        "fertilizer": [],
        "water": [],
        "light": [],
        "temperature": [],
        "humidity": [],
        "location": [],
    }
    for i in range(len(keys) - 1):
        key = keys[i]
        next_key = keys[i + 1]
        tmp_data: list[Range] = []
        for __r in mapped_data[key]:
            for __r2 in ctx.map_range(key, __r):
                tmp_data.append(__r2)
        mapped_data[next_key] = sorted(tmp_data, key=lambda r: r.start)
    print(
        f"Lower location value based on initial seed values is {min([r.start for r in mapped_data['location']])}"
    )
    return mapped_data
