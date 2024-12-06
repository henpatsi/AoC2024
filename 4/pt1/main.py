XMAS = "XMAS"

def check_xmas(lines, x, y, x_dir, y_dir):
    for i in range(len(XMAS)):
        cur_x = x + x_dir * i
        cur_y = y + y_dir * i
        if cur_y >= len(lines) or cur_x >= len(lines[y]) or cur_y < 0 or cur_x < 0:
            return 0
        if lines[cur_y][cur_x] != XMAS[i]:
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
            xmas_count += check_xmas(lines, x, y, 1, 0)
            xmas_count += check_xmas(lines, x, y, 0, 1)
            xmas_count += check_xmas(lines, x, y, -1, 0)
            xmas_count += check_xmas(lines, x, y, 0, -1)
            xmas_count += check_xmas(lines, x, y, 1, 1)
            xmas_count += check_xmas(lines, x, y, 1, -1)
            xmas_count += check_xmas(lines, x, y, -1, 1)
            xmas_count += check_xmas(lines, x, y, -1, -1)

    print(xmas_count)

if __name__ == '__main__':
    main()
