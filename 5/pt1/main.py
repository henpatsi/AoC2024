def check_rules(nums, rules):
    checked = set()

    for num in nums:
        checked.add(num)
        if num not in rules:
            continue
        for rule_num in rules[num]:
            if rule_num in checked:
                return False
    return True

def main():
    correct_line_sum = 0
    rules = {}

    input_file = open("input", "r")

    for line in input_file:
        stripped_line = line.strip()
        if stripped_line == "":
            break
        before, after = [int(c) for c in stripped_line.split("|")]
        if before not in rules:
            rules[before] = set()
        rules[before].add(after)
    
    for line in input_file:
        nums = [int(c) for c in line.strip().split(",")]
        if check_rules(nums, rules):
            correct_line_sum += nums[int((len(nums) - 1)/2)]
     
    print(correct_line_sum)

if __name__ == '__main__':
    main()