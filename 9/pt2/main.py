def print_blocks(line, indeces):
    blocks = []
    for i in range(len(line)):  
        for c in range(line[i]):
            if i % 2 == 0 and i < len(indeces) * 2:
                blocks.append(indeces[int(i / 2)])
            else:
                blocks.append(".")
    print(blocks)


def main():
    count = 0

    input_file = open("input", "r")

    line = [int(x) for x in input_file.readline().strip()]

    indeces = []
    for i in range(0, int((len(line) + 1) / 2)):
        indeces.append(i)

    end = len(line) - 1 if (len(line) - 1) % 2 == 0 else len(line) - 2
    i = end
    while i >= 0:
        for j in range(1, len(line), 2):
            if j >= i:
                break
            if line[j] >= line[i]:
                move_amount = line[i]
                line[j] -= move_amount
                line[i - 1] += move_amount
                if i != end:
                    line[i - 1] += line[i + 1]

                if i != end:
                    del line[i + 1]
                del line[i]

                line.insert(j, move_amount)
                line.insert(j, 0)

                index = indeces[int(i / 2)]
                del indeces[int(i / 2)]
                indeces.insert(int((j + 1) / 2), index)

                i += 2
                break
        i -= 2

    blocks = []
    for i in range(len(line)):  
        for c in range(line[i]):
            if i % 2 == 0 and i < len(indeces) * 2:
                blocks.append(indeces[int(i / 2)])
            else:
                blocks.append(".")

    checksum = 0
    for i in range(len(blocks)):
        if blocks[i] == ".":
            continue
        checksum += i * blocks[i]
    
    print(checksum)


if __name__ == '__main__':
    main()
