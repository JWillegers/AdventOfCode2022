from readFile import *


def part1(instructions):
    visited = set()
    visited.add((0, 0))
    head = (0, 0)
    tail = (0, 0)
    for motion in instructions:
        direction, amount_of_steps = motion.split(' ')
        for step in range(int(amount_of_steps)):
            # change position head
            if direction == 'R':
                head = (head[0], head[1] + 1)
            elif direction == 'L':
                head = (head[0], head[1] - 1)
            elif direction == 'U':
                head = (head[0] + 1, head[1])
            elif direction == 'D':
                head = (head[0] - 1, head[1])
            else:
                exit(9)

            # check if we need to change tail position
            if head[0] - tail[0] > 1:
                tail = (head[0] - 1, head[1])
            elif head[0] - tail[0] < -1:
                tail = (head[0] + 1, head[1])
            elif head[1] - tail[1] > 1:
                tail = (head[0], head[1] - 1)
            elif head[1] - tail[1] < -1:
                tail = (head[0], head[1] + 1)
            visited.add(tail)

    return len(visited)


def part2(instructions):
    visited = set()
    visited.add((0, 0))
    rope = [(0, 0) for x in range(10)]
    for motion in instructions:
        direction, amount_of_steps = motion.split(' ')
        for step in range(int(amount_of_steps)):
            # change position head
            if direction == 'R':
                rope[0] = (rope[0][0], rope[0][1] + 1)
            elif direction == 'L':
                rope[0] = (rope[0][0], rope[0][1] - 1)
            elif direction == 'U':
                rope[0] = (rope[0][0] + 1, rope[0][1])
            elif direction == 'D':
                rope[0] = (rope[0][0] - 1, rope[0][1])
            else:
                exit(9)

            # check if we need to change tail position
            for i in range(1, len(rope)):
                if rope[i - 1][0] - rope[i][0] > 1:
                    if rope[i - 1][1] - rope[i][1] > 1:
                        rope[i] = (rope[i - 1][0] - 1, rope[i - 1][1] - 1)
                    elif rope[i - 1][1] - rope[i][1] < -1:
                        rope[i] = (rope[i - 1][0] - 1, rope[i - 1][1] + 1)
                    else:
                        rope[i] = (rope[i - 1][0] - 1, rope[i - 1][1])
                elif rope[i - 1][0] - rope[i][0] < -1:
                    if rope[i - 1][1] - rope[i][1] > 1:
                        rope[i] = (rope[i - 1][0] + 1, rope[i - 1][1] - 1)
                    elif rope[i - 1][1] - rope[i][1] < -1:
                        rope[i] = (rope[i - 1][0] + 1, rope[i - 1][1] + 1)
                    else:
                        rope[i] = (rope[i - 1][0] + 1, rope[i - 1][1])
                elif rope[i - 1][1] - rope[i][1] > 1:
                    rope[i] = (rope[i - 1][0], rope[i - 1][1] - 1)
                elif rope[i - 1][1] - rope[i][1] < -1:
                    rope[i] = (rope[i - 1][0], rope[i - 1][1] + 1)
            visited.add(rope[-1])

    return len(visited)


if __name__ == '__main__':
    test_file_small = line_str(91, True)
    test_file_large = line_str(92, True)
    assert(13 == part1(test_file_small))
    assert(1 == part2(test_file_small))
    assert(36 == part2(test_file_large))
    file = line_str(9)
    print('part1:', part1(file))
    print('part2:', part2(file))
