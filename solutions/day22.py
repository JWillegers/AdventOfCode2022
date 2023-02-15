from readFile import *
import re

puzzle_input = '12R4L24R35L16L33R16L45L40L50L42L6R7L33L42L23L7R37R23R7L49R29R12L7R43R22R25L39R36L23L16L10R48R31L41R29L32R45L24L48R32L42L47L27L31R4R31R47L3L1L39L4R21R13L42R28L3L42L1R28L30R4L23R5R23R6L41R9R6R1L41R44R12R10L24R30L47R41L33L38R38L34R43L11L8R25L14L31R48R39L47L4L5L23R31L26L2R24L47R6L49R39L50L18L11L6R28R35L37L29L5R18R19L7L16L2R1L13R28L46R42L48R19R1R41L42R12L20R27L21L48L6R45L35L43L47L15L12R21L39L7R24L39R26L6L9R22R16R24L3R3L28L22R11L11L8L44L35L44R7L48R31L13L15R46L39R14L19L27L48L15R33L24R43R36L32R2R14L27R20R37L42R27R27L14R47R1R50R34R33R47R3L24R10R9L35R37R19R27R5L43R2R19L33L46L7L45R20R7L3L21R49L2L49L31R24L13L31R9R20R36R28R28L11L23R13R39L5R3R23L34R9L32L7L4R21L27L9R19R37L32L5L17L49L14R29R12R31R31L33R10L28R35R46R37R20L4L43L34L4R19R48L15R14L45R46L24R3R30L39L23L42L23L48L46R33R40R4L29R45R44R23L23R17R1R22R39R17L40L6R19L13L45R25R22R50L19R9R7R23R50L16L18R33R8L23R28R6R24L2L7R25R19R42R49L28L18L47R46L15L23R34R30R42L38R16L45R27R4R16L4R45R5L41L42L20R44L8R50L45R2R9L7R26L38R26R29R47L26R24L13R37L17R12L50R22R24L22L32R19L1L5R2R48R40R9R16L28R33R11L3R47R35L34R48L45R44L1L14R45L34L35L44R22R32R31R5L5R30L7L27R23L9L30R48R26L30L36L11L48L49R16L38R35L45L39L9L32L46L35L43L44R35L23L17R30L5R38L24L29L39L27L15R22R40L16L37L10R19R40R17R9R30L1L31R31L24R27L25L12L37R8L43L41L40R34R11L28L48R9L14R44L43L32L39L17R38R40R13L45R46L46L39R7R30R13L13R37R46L45R11R19L25R39L28L43R21L23L4L17R9R32L37L5L19R22R17R12L20L13L29L35L7R47L44R1L29R4L6R34R50L3R39L44L24L29L22L13R22R27L33L41L38L2R16L20R14L20R34R26L27L25R26L48R8L26L30L21L18R38L31R36R30R44R27R46R12L13L41R39R21R38R11R44L23L28R38L14L43L3L34L50R28L13R17L32L49R47R47L34R35R48R22R15L35R43L1L22L48L31R34R1R22R1R12L49L38R1L26R13R48L5L37R33L3L25R38R46L7L3R40R28R14R18L4L30L43R3L5L42R3R4R40R9L41L22L13R46R48L30R27R24L21R17L9R18L25R15R13R3L42L28R48L6L8L17L32R26L33R26R36R1R50L26R9R5R18L33L9L39R35L34R9L43L42R17L49R49R9R33R24L23R3R20L22R40R10L5R47L43L32L34R33R21L25L20L31L19R35R21L24R13R26R1L15R19L21R48R38R35R26R41L5R5R12L31L48R46L43R41L42L32R14R17L33L29L41R5R29L49L47L27L1R6R43L10L40R29R14L20L50L31L26L33L35L3R45L17L35R8R18L16R34R43L21L30R39L40L20R22R20R42L29L48R46L1R11L8L16R19R42R13R22R23L26R23L6L21L39R46R23R30R41L35R16L19R38L10R47R6L34L30R27R46R31L8L32R21R27R10R3R5R28L2R45R41R6R40R47L15R50R29L40R37R47L22L47L3R36R4L42L21L13R9L17R20L50R35L25L49R47R3R6L38L43L42R12L16R27L42L9L17R35R49R32R45L37L35L29R10R28R10R49L1R14L25L39L9R8R8R12L45R31R20L39R33L19L11L24R15L46R37R18L6R33L18R3L47R29L38R27R13L31L29L4R10R47L12L35R30R1L11L49R41R48L17R19L3R18R25L18L27R13R20R35L10L21R36L14L2R28L43R16L33R2L29L30L15L22L11L7R20R3R4L20L39L3R25R3R18R22R50L4L23L13R19R33L3R26R16L48R43L47R10L29R2R20R26R32L42R3R27R46L47L39R49L3L23R18R49L5L15L27R47L8L15L29L6R35L31R1R21L39L48L50L11L25L30R48L21L2R47R26L46L29R37L11R10R7R34L27L47R12L24L1R10L38L37R21L24L12L32R12R13R8R22R7R6L19R42R45R5L31L5L29R11L24R7R49R2R16R12R36R3L23L13R14R29L7L41L6R16L46L39R42R17R15L37R3L31L19L21R47L23R47R4L48R18R10L15R15L14R46L40R42L32R46L33R18L11L15R42R11R30L7L27L49L45R24L42R20R3L30R19R9R2L1L6L18R15L7R23L24R40R17L14R23L28R2R39L45L15R2R41R36L23L37L36L47L31L32R35L27R28R24L24R6L43L23R20R44R27R18L18L22L19L33R12R24L41R3L13R17L44R8L1L24L39L4L47R43R35L2L36L27R30L11R45L2L19R42L33L32R26R40R49L38R45R31R38R26R7R34L4R22L11R43R35L2L44R12R29R36R49R20R41L30L42R36R11L29R48L12R15R28L31R28R28L33L30R39R16R10R41L49R31R46L6L29L17R27R20R28L40R31L30L7L22L24L3R28R23L25L14R7L19R30R6R31L41R25R42L40L8R44R47L32R48L20R29L43L42R1R31R16R47L16R28L47L48L16L24L19R29R44L8L24L13L48R31L30L19L20L42R13L38L26L38R18L18R35L41R30L4R43R44R40L5R1L42R24R20L38R14L18R7R17R36R49L7R44L30R1R27R6L45L23R28R47L17L28L6L9L18R29L42L26L11L28R1L16R31R23R9R7L19L7R10R34R28L44L5L15L11L29L11R8L35L33R3R11R23R16L30L25R29R4L41R26L24L42R8L26R36R49L18L7R23L38R23R33R20R27R14L6L25R39L13R12L44R18R49L15L37L26R24R30L11L47L47L35R20L22R2L6L21R48R47R24L11R5R36L8R42R40R13L25L28R44R40L44L4L5R39L48R5R18R17R41L24L37R45R35R7L28L45R32R19L50L31R4L47R18R26R21R22R5R43L25R13L47R5R16R42L14L26R2R17L1R20L22L7R12R5L34R48L10L24L28R47R18L25R12L9R45R3L33R1L11L2L44L50R13R22R30R7R18L36R37R5R28R32R18R46L8R30L15L11R32R8R32L29L13L19L14R45R13R19R46L10L2R3R12L43L47R18R4L46R12R39R21R48L7R49L1L15L7L24R49R26L3R16R20L35R22R4L14R33R29L37R6L11L37R48R23L45R41L12L46R49L46L16R21R43L22L48R31L16L44R22L20R12L34R47L47R26L44L1L10L10R3R15R19R1R1R14R9L36L30L42L5L5R19R4R17L38R19L18R32L42L37L28L8L12R1R19L45L23R47R11R4L10R41R4R32L23R36R49R37L19L7R24L25L21L43R42R17R25R3L21R22L48L18L23L42R38R12L32L38R27L25R17L32L11L47R2L22R1L39R30L12L21L10R6L16L1R4L37L46R2R45L50L12R32L32R27L11R36L5L28L16L6R29R4R6R7L39R28L2L23L9R40L50R10L10R44L36L41L3R37L38R37R5L7R21L36R2L28L36R4R39L25R26L49L8R42L11L26R30L5R36R47R20R47L2R26L22L40L32R35L47R21R48R5L18L46R40R2R46L27R10R33R13R7L22L21R4R30L25L24L13R4R18L18R46L6R50L21R21R40L4R43R8R45R21L30L40L20R27R46R19R35R46L1L37R33L25L46R23L3L45L34L19L4R15L41L8R18L16R15R26L43L17R21R43L13R26L44R5L1R47R37R8L45L38R36R22L2R6R36R7R48L25L30L33L10L19L27L26L50L22L12R40L30R39R15R28R44L4L8R2R2L36L1L44L9L36L38R30R33R16R49L27L40R29R4R16L42R16L42L35R22R30L29L9L45R33R18L1R16R23R42R4L19R22R24R26L26L31L14R33L7L42R42R30R33R49L4R3R24L11L22R18R2L25L38L41L46L14R38L23R14L3L22L19R34L12L25R6L1R8R29R43L26L20L5R7R21R29R36R2L46L23L4L47R20R30L23L35R18L19L26R47L40R46R36R47L25R38R43R38R4R6R12R47L27L10L39L17R50R4R25L11R35L39L14L36R36L18R41R27L44R40L24L48L46L37L5L4R49R18L27L38R6R39R32L7R11L32R15R28L7L7R46L46R36R26R18R10L26R44R7R47L45R15L19R25R15L47R16L3R27R30L5L11L15R39R36R22R41R22R27R18R10R31R8L31L11L16L42L35R32R37L34L33R25R41L11R2R13L7R15R5R50R44L44R33R31L49L40L6L41R40L23L39R16R4L8L3L42L43R46L8R17R11L36L18R34L38R41R1L4L43L15L26R38L21R43R48R14L40L47R21L17L50R42R43L40R34L44R24L8R50L16R16L43R24R45L22L42L34L42L26L25R20R17R9L22L26L27L38R9L32R17L31L39L7R9L23L35R7'
test_input = '10R5L5R10L4R5L5'
direction_scores = {
        'R': 0,
        'D': 1,
        'L': 2,
        'U': 3,
    }
rotate_clockwise = {
    'R': 'D',
    'D': 'L',
    'L': 'U',
    'U': 'R'
}
rotate_counter_clockwise = {
    'D': 'R',
    'L': 'D',
    'U': 'L',
    'R': 'U'
}
free_space = '.'
rock = '#'


def solution(my_map, path, part1):
    direction = 'R'
    location = [0, 0]
    for i in range(len(my_map[0])):
        if my_map[0][i] == '.':
            location = [0, i]
            break
    for instruction in path:
        if type(instruction) is int:
            if direction == 'R':
                location, direction = walk(my_map, location, 0, 1, instruction, part1, direction)
            elif direction == 'D':
                location, direction = walk(my_map, location, 1, 0, instruction, part1, direction)
            elif direction == 'L':
                location, direction = walk(my_map, location, 0, -1, instruction, part1, direction)
            elif direction == 'U':
                location, direction = walk(my_map, location, -1, 0, instruction, part1, direction)
        elif instruction == 'R':
            direction = rotate_clockwise[direction]
        else:
            direction = rotate_counter_clockwise[direction]

    return 1000 * (location[0] + 1) + 4 * (location[1] + 1) + direction_scores[direction]


def walk(my_map, location, d_row, d_col, n_steps, part1, direction):
    for i in range(n_steps):
        wrap_around = True
        row = location[0]
        col = location[1]
        if not(row + d_row == -1 or row + d_row == len(my_map) or
               col + d_col == -1 or col + d_col == len(my_map[row])):
            if my_map[row + d_row][col + d_col] == free_space:
                wrap_around = False
                location[0] += d_row
                location[1] += d_col
            elif my_map[row + d_row][col + d_col] == rock:
                break

        if wrap_around:
            if part1:
                location = part1_wrap(my_map, row, col, d_row, d_col, location)
            else:
                location, direction, d_row, d_col = part2_wrap(my_map, row, col, d_row, d_col, direction)

    return location, direction


# Should work with every input
def part1_wrap(my_map, row, col, d_row, d_col, location):
    if d_row == 1:
        for j in range(len(my_map)):
            if my_map[j][col] == rock:
                break
            elif my_map[j][col] == free_space:
                location[0] = j
                break
    elif d_row == -1:
        for j in range(len(my_map) - 1, -1, -1):
            if my_map[j][col] == rock:
                break
            elif my_map[j][col] == free_space:
                location[0] = j
                break
    elif d_col == 1:
        for j in range(len(my_map[row])):
            if my_map[row][j] == rock:
                break
            elif my_map[row][j] == free_space:
                location[1] = j
                break
    elif d_col == -1:
        for j in range(len(my_map[row]) - 1, -1, -1):
            if my_map[row][j] == rock:
                break
            elif my_map[row][j] == free_space:
                location[1] = j
                break
    return location


# Works only for my input
def part2_wrap(my_map, row, col, d_row, d_col, direction):
    '''
     12
     3
    54
    6
    '''
    location = [row, col]
    if row < 50 and col < 100:
        # side 1
        if row == 0 and direction == 'U':
            # go to left side of 6
            new_row = col - 50 + 150
            if my_map[new_row][0] == free_space:
                location = [new_row, 0]
                direction = 'R'
                d_row = 0
                d_col = 1
        elif col == 50 and direction == 'L':
            # go to left side of 5 (mirrored)
            new_row = 49 - row + 100
            if my_map[new_row][0] == free_space:
                location = [new_row, 0]
                direction = 'R'
                d_row = 0
                d_col = 1
    elif col >= 100:
        # side 2
        if row == 0 and direction == 'U':
            # go to bottom of 6
            new_col = col - 100
            if my_map[199][new_col] == free_space:
                location = [199, new_col]
                assert(direction == 'U')
                assert(d_col == 0)
                assert(d_row == -1)
        elif col == 149 and direction == 'R':
            # go to right of 4 (mirrored)
            new_row = 49 - row + 100
            if my_map[new_row][99] == free_space:
                location = [new_row, 99]
                direction = 'L'
                d_col = -1
                d_row = 0
        elif row == 49 and direction == 'D':
            # go to right of 3
            row = col - 100 + 50
            if my_map[row][99] == free_space:
                location = [row, 99]
                direction = 'L'
                d_col = -1
                d_row = 0
    elif 50 <= row < 100:
        # side 3
        if col == 50 and direction == 'L':
            # go to top of 5
            new_col = row - 50
            if my_map[100][new_col] == free_space:
                location = [100, new_col]
                direction = 'D'
                d_col = 0
                d_row = 1
        elif col == 99 and direction == 'R':
            # go to bottom of 2
            new_col = row - 50 + 100
            if my_map[49][new_col] == free_space:
                location = [49, new_col]
                direction = 'U'
                d_col = 0
                d_row = -1
    elif 100 <= row < 150 and 50 <= col:
        # side 4
        if col == 99 and direction == 'R':
            # go to right of side 2 (mirrored)
            new_row = 49 - (row - 100)
            if my_map[new_row][149] == free_space:
                location = [new_row, 149]
                direction = 'L'
                d_col = -1
                d_row = 0
        elif row == 149 and direction == 'D':
            # go to right of 6
            new_row = col - 50 + 150
            if my_map[new_row][49] == free_space:
                location = [new_row, 49]
                direction = 'L'
                d_col = -1
                d_row = 0
    elif row < 150:
        # side 5
        if row == 100 and direction == 'U':
            # go to left of 3
            new_row = col + 50
            if my_map[new_row][50] == free_space:
                location = [new_row, 50]
                direction = 'R'
                d_row = 0
                d_col = 1
        if col == 0 and direction == 'L':
            # go to left of 1 (mirrored)
            new_row = 49 - (row - 100)
            if my_map[new_row][50] == free_space:
                location = [new_row, 50]
                direction = 'R'
                d_row = 0
                d_col = 1
    else:
        # side 6
        if col == 0 and direction == 'L':
            # go to top of 1
            new_col = row - 150 + 50
            if my_map[0][new_col] == free_space:
                location = [0, new_col]
                direction = 'D'
                d_row = 1
                d_col = 0
        elif col == 49 and direction == 'R':
            # go to bottom of 4
            new_col = row - 150 + 50
            if my_map[149][new_col] == free_space:
                location = [149, new_col]
                direction = 'U'
                d_row = -1
                d_col = 0
        elif row == 199 and direction == 'D':
            # go to top of 2
            new_col = col + 100
            if my_map[0][new_col] == free_space:
                location = [0, new_col]
                direction = 'D'
                d_row = 1
                d_col = 0

    assert(my_map[location[0]][location[1]] == free_space)
    return location, direction, d_row, d_col


if __name__ == '__main__':
    test_file = grid(22, test=True)
    test_path = re.split(r'([RL])', test_input)
    for o in range(len(test_path)):
        if test_path[o] != 'R' and test_path[o] != 'L':
            test_path[o] = int(test_path[o])
    row_0 = len(test_file[0])
    for line in test_file:
        while len(line) < row_0:
            line.append('')
    assert(solution(test_file, test_path, True) == 6032)
    file = grid(22)
    # split input on R and L, whilst keeping R and L in the list -> result [int, 'R' or 'L', int, 'R' or 'L', ... , 'R' or 'L']
    global_path = re.split(r'([RL])', puzzle_input)
    for o in range(len(global_path)):
        if global_path[o] != 'R' and global_path[o] != 'L':
            global_path[o] = int(global_path[o])
    row_0 = len(file[0])
    for line in file:
        while len(line) < row_0:
            line.append('')
    print('part1:', solution(file, global_path, True))
    print('part2:', solution(file, global_path, False))  # 133067 too high, 3271 too low
