import itertools

def try_operate(sum, nums):

    operator_options = list(itertools.product([0, 1], repeat=len(nums) - 1))

    for operators in operator_options:
        test_sum = nums[0]
        for i in range(len(operators)):
            if operators[i] == 0:
                test_sum += nums[i + 1]
            else:
                test_sum *= nums[i + 1]
        if test_sum == sum:
            return sum

    return 0


def main():

    operatable_sums = 0

    input_file = open("input", "r")

    for line in input_file:
        sum, numstring = line.strip().split(":")
        nums = [int(c) for c in numstring.split()]
        operatable_sums += try_operate(int(sum), nums)

    print(operatable_sums)


if __name__ == '__main__':
    main()
