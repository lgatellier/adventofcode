from aoc.y23.day05 import parse_context


def main(lines: list[str]):
    ctx = parse_context(lines)
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
    mapped_data = {
        "seed": ctx.seeds,
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
        for value in mapped_data[key]:
            mapped_data[next_key].append(ctx.map_value(key, value))
    print(
        f"Lower location value based on initial seed values is {min(mapped_data['location'])}"
    )
    return mapped_data
