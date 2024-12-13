from collections import defaultdict

def blink(stones):
    new_stones = defaultdict(int)

    for num, count in stones.items():
        if num == 0:
            new_stones[1] += count
        elif len(str(num)) % 2 == 0:
            new_stones[int(str(num)[:len(str(num))//2])] += count
            new_stones[int(str(num)[len(str(num))//2:])] += count
        else:
            new_stones[num * 2024] += count

    return new_stones

def main():
    stones = {}

    input_file = open("input", "r")

    for line in input_file:
        for c in line.strip().split():
            c = int(c)
            if c not in stones:
                stones[c] = 0
            stones[c] += 1
    
    for _ in range(75):
        stones = blink(stones)

    print(stones)
    count = 0
    for value in stones.values():
        count += value
    print(count)

if __name__ == '__main__':
    main()
