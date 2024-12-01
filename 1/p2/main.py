def main():
    similarity_score = 0

    left_numbers = []
    right_numbers = []
    
    input_file = open("input", "r")
    for line in input_file:
        split_line = line.split()
        left_numbers.append(int(split_line[0]))
        right_numbers.append(int(split_line[1]))

    for i in range(len(left_numbers)):
        occurances = 0
        for j in range (len(right_numbers)):
            if left_numbers[i] == right_numbers[j]:
                occurances += 1
        similarity_score += left_numbers[i] * occurances
    
    print(similarity_score)

if __name__ == '__main__':
    main()