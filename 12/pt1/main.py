def search_region(lines, x, y, letter):
    if y < 0 or y >= len(lines) or x < 0 or x >= len(lines[y]):
        return 0, 1
    if lines[y][x] == letter.lower():
        return 0, 0
    if lines[y][x] != letter:
        return 0, 1
    
    area = 1
    perimeter = 0
    lines[y][x] = letter.lower()
    
    a1, p1 = search_region(lines, x + 1, y, letter)
    a2, p2 = search_region(lines, x - 1, y, letter)
    a3, p3 = search_region(lines, x, y + 1, letter)
    a4, p4 = search_region(lines, x, y - 1, letter)

    area += a1 + a2 + a3 + a4
    perimeter += p1 + p2 + p3 + p4

    return area, perimeter


def main():

    input_file = open("input", "r")

    lines = []

    for line in input_file:
        lines.append(list(line.strip()))

    price = 0

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x].islower():
                continue
            #print(f"x: {x}, y: {y}, letter: {lines[y][x]}")
            area, perimeter = search_region(lines, x, y, lines[y][x])
            #print(f"Area: {area}, Perimeter: {perimeter}")
            price += area * perimeter
    
    print(price)

if __name__ == '__main__':
    main()
