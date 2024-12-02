def check_safe(split_line):
    if len(split_line) == 0 or len(split_line) == 1:
        return 0

    change_dir = 0

    for i in range(len(split_line) - 1):
        diff = int(split_line[i + 1]) - int(split_line[i])
        if diff == 0 or abs(diff) > 3:
            return 0
        if change_dir == 0:
            change_dir = diff
        if change_dir > 0 and diff < 0:
            return 0
        if change_dir < 0 and diff > 0:
            return 0

    return 1

def main():
    safe_count = 0
    
    input_file = open("input", "r")
    
    for line in input_file:
        split_line = line.split()
        safe_count += check_safe(split_line)
    
    print(safe_count)

if __name__ == '__main__':
    main()
