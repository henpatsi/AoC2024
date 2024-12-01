def main():
    distance_sum = 0
    left_numbers = []
    right_numbers = []
    
    input_file = open("input", "r")
    for line in input_file:
        split_line = line.split()
        left_numbers.append(split_line[0])
        right_numbers.append(split_line[1])
    
    left_numbers.sort()
    right_numbers.sort()

    for i in range(len(left_numbers)):
        distance_sum += abs(int(left_numbers[i]) - int(right_numbers[i]))
    
    print(distance_sum)

if __name__ == '__main__':
    main()