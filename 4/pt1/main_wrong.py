XMAS = "XMAS"

def find_xmases(lines, x, y, i):
    xmas_count = 0
    if i >= len(XMAS) or y >= len(lines) or x >= len(lines[y]):
        return 0
    if i < 0 or x < 0:
        return 0
    char = lines[y][x]
    if char != XMAS[i]:
        return 0
    else:
        print(char, x, y)
    if i == len(XMAS) - 1:
        return 1
    xmas_count += find_xmases(lines, x + 1, y, i+1)
    xmas_count += find_xmases(lines, x - 1, y, i+1)
    xmas_count += find_xmases(lines, x, y + 1, i+1)
    xmas_count += find_xmases(lines, x, y - 1, i+1)
    xmas_count += find_xmases(lines, x + 1, y + 1, i+1)
    xmas_count += find_xmases(lines, x - 1, y + 1, i+1)
    xmas_count += find_xmases(lines, x + 1, y - 1, i+1)
    xmas_count += find_xmases(lines, x - 1, y - 1, i+1)
    return xmas_count

def main():
    xmas_count = 0

    lines = []

    input_file = open("input2", "r")

    for line in input_file:
        lines.append(line.strip())

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            xmas_count += find_xmases(lines, x, y, 0)

    print(xmas_count)

if __name__ == '__main__':
    main()
