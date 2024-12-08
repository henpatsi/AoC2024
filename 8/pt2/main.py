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
        if len(positions) < 2:
            continue
        for position in positions:
            frequency_positions.add(position)
            for other_position in positions:
                if position == other_position:
                    continue
                diff = (position[0] - other_position[0], position[1] - other_position[1])
                new_position = (position[0] + diff[0], position[1] + diff[1])
                while new_position[0] >= 0 and new_position[1] >= 0 and new_position[0] <= y and new_position[1] < len(stripped_line):
                    frequency_positions.add(new_position)
                    new_position = (new_position[0] + diff[0], new_position[1] + diff[1])

    print(len(frequency_positions))


if __name__ == '__main__':
    main()
