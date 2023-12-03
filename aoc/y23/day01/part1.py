# write a function which reads file "input" line by line
def read_file(input):
    with open(input, "r") as f:
        lines = f.readlines()
        return lines


def get_line_calibration_value(line):
    # process all line characters one by one
    first_digit = None
    last_digit = None
    for i in range(len(line)):
        # if the character is a digit
        if line[i].isdigit():
            if not first_digit:
                first_digit = line[i]
            last_digit = line[i]
    return int(f"{first_digit}{last_digit}")


# sum all calibration values for file named "input"
def sum_calibration_values(input):
    lines = read_file(input)
    sum = 0
    for line in lines:
        calibration_value = get_line_calibration_value(line)
        print(f"{line[0:-1]} : {calibration_value}")
        sum += calibration_value
    return sum


# main function, which computes sum_calibration_values for file
# which named is passed in script argument
def main(input_file="input"):
    sum = sum_calibration_values(input_file)
    print(f"Sum of calibration values is {sum}")
    return sum


if __name__ == "__main__":
    import sys

    main(sys.argv[1] if len(sys.argv) > 1 else None)
