def read_file(input):
    with open(input, "r") as f:
        return [line.strip() for line in f.readlines()]
