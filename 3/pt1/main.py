import re

REGEX_PATTERN = "mul\([0-9]{1,3},[0-9]{1,3}\)"

def get_line_muls(line):
    line_mul_sum = 0

    muls = re.search(REGEX_PATTERN, line)
    while muls != None:
        nums = line[muls.start() + 4:muls.end() - 1].split(",")
        line_mul_sum += int(nums[0]) * int(nums[1])
        line = line[muls.end() - 1:]
        muls = re.search(REGEX_PATTERN, line)

    return line_mul_sum

def main():
    mul_sum = 0

    input_file = open("input", "r")

    for line in input_file:
        mul_sum += get_line_muls(line)

    print(mul_sum)

if __name__ == '__main__':
    main()
