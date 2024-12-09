def main():
    count = 0

    input_file = open("input", "r")

    line = [int(x) for x in input_file.readline().strip()]

    blocks = []

    for i in range(len(line)):  
        for c in range(line[i]):
            if i % 2 == 0:
                blocks.append(i / 2)
            else:
                blocks.append(".")
    
    back_index = len(blocks) - 1
    for i in range(len(blocks)):
        if back_index <= i:
            break
        if blocks[i] != ".":
            continue
        blocks[i] = blocks[back_index]
        blocks[back_index] = "."
        while(blocks[back_index] == "."):
            back_index -= 1
    
    checksum = 0

    for i in range(len(blocks)):
        if blocks[i] == ".":
            break
        checksum += i * blocks[i]
    
    print(checksum)

if __name__ == '__main__':
    main()
