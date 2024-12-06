import re

REGEX_PATTERN = "mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)"

mul_enabled = True

def get_line_muls(line):
    line_mul_sum = 0
    global mul_enabled

    match = re.search(REGEX_PATTERN, line)
    while match != None:
        match_string = match.group(0)
        if mul_enabled and line[match.start()] == "m":
            nums = line[match.start() + 4:match.end() - 1].split(",")
            line_mul_sum += int(nums[0]) * int(nums[1])
        elif mul_enabled and match_string == "don't()":
            mul_enabled = False
        elif not mul_enabled and match_string == "do()":
            mul_enabled = True
        line = line[match.end() - 1:]
        match = re.search(REGEX_PATTERN, line)

    return line_mul_sum

def main():
    mul_sum = 0

    input_file = open("input", "r")

    for line in input_file:
        mul_sum += get_line_muls(line)

    print(mul_sum)

if __name__ == '__main__':
    main()
