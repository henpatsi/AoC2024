UP = (-1, 0)
RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)

def main():

    lines = []
    unique_positions = 0
    guard_pos = [0, 0]
    guard_dir_index = 0
    guard_dirs = [UP, RIGHT, DOWN, LEFT]

    input_file = open("input", "r")

    for i, line in enumerate(input_file):
        lines.append(list(line.strip()))
        if "^" in line:
            guard_pos = [i, line.index("^")]
            lines[guard_pos[0]][guard_pos[1]] = "."

    current_dir = guard_dirs[guard_dir_index]

    while 1:
        y = guard_pos[0]
        x = guard_pos[1]

        if lines[y][x] == ".":
            lines[y][x] = "X"
            unique_positions += 1
        
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
    
    print(unique_positions)

        

if __name__ == '__main__':
    main()