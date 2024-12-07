#!/bin/bash

echo "def main():
    count = 0

    input_file = open(\"input\", \"r\")

    for line in input_file:
        print(line)

if __name__ == '__main__':
    main()" > main.py