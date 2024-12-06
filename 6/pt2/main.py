UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)

def get_path(lines, guard_pos):
    guard_dir_index = 0
    guard_dirs = [UP, RIGHT, DOWN, LEFT]

    current_dir = guard_dirs[guard_dir_index]

    while 1:
        y = guard_pos[0]
        x = guard_pos[1]

        if lines[y][x] == ".":
            lines[y][x] = "X"
        
        new_y = y + current_dir[0]
        new_x = x + current_dir[1]

        if new_y < 0 or new_x < 0 or new_y >= len(lines) or new_x >= len(lines[0]):
            break

        while lines[new_y][new_x] == "#":
            guard_dir_index = (guard_dir_index + 1) % len(guard_dirs)
            current_dir = guard_dirs[guard_dir_index]
            new_y = y + current_dir[0]
            new_x = x + current_dir[1]
        
        guard_pos[0] = new_y
        guard_pos[1] = new_x
    
    return lines


def check_loop(lines, guard_pos, max_path_length, obstacle_pos):
    moves = 0
    guard_dir_index = 0
    guard_dirs = [UP, RIGHT, DOWN, LEFT]

    current_dir = guard_dirs[guard_dir_index]

    while moves < max_path_length:
        y = guard_pos[0]
        x = guard_pos[1]
        
        new_y = y + current_dir[0]
        new_x = x + current_dir[1]

        if new_y < 0 or new_x < 0 or new_y >= len(lines) or new_x >= len(lines[0]):
            return False

        while lines[new_y][new_x] == "#" or (new_y == obstacle_pos[0] and new_x == obstacle_pos[1]):
            guard_dir_index = (guard_dir_index + 1) % len(guard_dirs)
            current_dir = guard_dirs[guard_dir_index]
            new_y = y + current_dir[0]
            new_x = x + current_dir[1]
        
        guard_pos[0] = new_y
        guard_pos[1] = new_x

        moves += 1

    return True


def main():

    loop_count = 0
    lines = []

    input_file = open("input", "r")

    for i, line in enumerate(input_file):
        lines.append(list(line.strip()))
        if "^" in line:
            guard_pos = [i, line.index("^")]
            lines[guard_pos[0]][guard_pos[1]] = "."

    lines = get_path(lines, guard_pos.copy())

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "X" and (check_loop(lines, guard_pos.copy(), 10000, (y, x))):
                loop_count += 1

    print(loop_count)
        

if __name__ == '__main__':
    main()