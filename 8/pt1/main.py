def main():
    symbol_positions = {}
    frequency_positions = set()
    frequenct_count = 0

    input_file = open("input", "r")

    for y, line in enumerate(input_file):
        stripped_line = line.strip()

        for x in range(len(stripped_line)):
            symbol = stripped_line[x]
            if symbol == '.':
                continue

            if symbol not in symbol_positions:
                symbol_positions[symbol] = set()
            symbol_positions[symbol].add((y, x))


    for symbol, positions in symbol_positions.items():
        for position in positions:
            for other_position in positions:
                if position == other_position:
                    continue
                diff = (position[0] - other_position[0], position[1] - other_position[1])
                frequency_positions.add((position[0] + diff[0], position[1] + diff[1]))


    for position in frequency_positions:
        if position[0] < 0 or position[1] < 0:
            continue
        if position[0] > y  or position[1] >= len(stripped_line):
            continue
        frequenct_count += 1


    print(frequenct_count)


if __name__ == '__main__':
    main()
