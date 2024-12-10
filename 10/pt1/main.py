def find_trails(trails, lines, x, y, i):
    if y < 0  or x < 0 or y >= len(lines) or x >= len(lines[y]):
        return
    if lines[y][x] != i:
        return
    if i == 9:
        trails.add((x, y))
        return
    find_trails(trails, lines, x + 1, y, i + 1)
    find_trails(trails, lines, x - 1, y, i + 1)
    find_trails(trails, lines, x, y + 1, i + 1)
    find_trails(trails, lines, x, y - 1, i + 1)
    return


def main():
    lines = []
    input_file = open("input", "r")
    trail_count = 0

    for line in input_file:
        lines.append([int(c) for c in line.strip()])
    
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            trails = set()
            find_trails(trails, lines, x, y, 0)
            trail_count += len(trails)
    
    print(trail_count)

if __name__ == '__main__':
    main()
