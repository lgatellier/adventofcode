import regex as re

# this regex matches digits, and also digits spelled in letter, like one, two, three, etc.
REGEXP_DIGITS_SPELLED_IN_LETTERS = (
    r"(\d|one|two|three|four|five|six|seven|eight|nine|ten)"
)
LETTERS_TO_DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
}


# write a function which reads file "input" line by line
def read_file(input):
    with open(input, "r") as f:
        lines = f.readlines()
        return lines


def get_line_calibration_value(line):
    for i in range(len(line)):
        # all matches of REGEXP_DIGITS_SPELLED_IN_LETTERS in the line
        matches = re.findall(REGEXP_DIGITS_SPELLED_IN_LETTERS, line, overlapped=True)
        first_digit = convert_letters_to_digit(matches[0])
        last_digit = convert_letters_to_digit(matches[-1])
    return int(f"{first_digit}{last_digit}")


def convert_letters_to_digit(letters):
    if letters.isnumeric():
        return int(letters)
    return LETTERS_TO_DIGITS[letters]


# sum all calibration values for file named "input"
def sum_calibration_values(input):
    lines = read_file(input)
    sum = 0
    for line in lines:
        calibration_value = get_line_calibration_value(line)
        print(f"{line[0:-1]} : {calibration_value}")
        sum += calibration_value
    return sum


# main function, which computes sum_calibration_values for file which named is passed in script argument
def main(input_file="input"):
    sum = sum_calibration_values(input_file)
    print(f"Sum of calibration values is {sum}")
    return sum


if __name__ == "__main__":
    import sys

    main(sys.argv[1] if len(sys.argv) > 1 else None)
