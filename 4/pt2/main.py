def check_xmas(lines, x, y):
    if lines[y][x] != "A":
        return 0
    if y < 1 or x < 1 or y >= len(lines) - 1 or x >= len(lines[y]) - 1:
        return 0
    
    top_left = lines[y - 1][x - 1]
    top_right = lines[y - 1][x + 1]
    bottom_left = lines[y + 1][x - 1]
    bottom_right = lines[y + 1][x + 1]

    if not (top_left == "M" and bottom_right == "S") and not (top_left == "S" and bottom_right == "M"):
        return 0
    if not (top_right == "M" and bottom_left == "S") and not (top_right == "S" and bottom_left == "M"):
        return 0

    return 1

def main():
    xmas_count = 0

    lines = []

    input_file = open("input", "r")

    for line in input_file:
        lines.append(line.strip())

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            xmas_count += check_xmas(lines, x, y)

    print(xmas_count)

if __name__ == '__main__':
    main()
