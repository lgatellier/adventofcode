state = {
    "verbose": False,
}


def read_file(input):
    with open(input, "r") as f:
        return [line.strip() for line in f.readlines()]


def verbose(message, **kwargs):
    if state["verbose"]:
        print(message.format(**kwargs))
