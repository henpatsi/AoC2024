def main():
    xmas_count = 0

    letters = []

    input_file = open("input", "r")

    for line in input_file:
        letters.append(line.strip())


    print(xmas_count)

if __name__ == '__main__':
    main()
