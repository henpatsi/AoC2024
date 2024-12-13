def blink(stones):
    new_stones = []

    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            new_stones.append(int(str(stone)[:len(str(stone))//2]))
            new_stones.append(int(str(stone)[len(str(stone))//2:]))
        else:
            new_stones.append(stone * 2024)
    return new_stones

def main():
    stones = []

    input_file = open("input", "r")

    for line in input_file:
        stones = [int(s) for s in line.strip().split()]

    for _ in range(8):
        stones = blink(stones)
        print(stones)

    print(len(stones))

if __name__ == '__main__':
    main()
