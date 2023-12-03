state = {
    "verbose": False,
}


def read_file(input):
    with open(input, "r") as f:
        return [line.strip() for line in f.readlines()]


def verbose(message, **kwargs):
    if state["verbose"]:
        print(message.format(**kwargs))


def main(main_function: callable):
    import sys

    return main_function(sys.argv[1] if len(sys.argv) > 1 else None)
