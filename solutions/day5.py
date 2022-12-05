import copy
from readFile import *


def part1(instructions, stack):
    for line in instructions:
        if 'move' in line:
            split = line.split(' ')
            amount = int(split[1])
            start = int(split[3])
            end = int(split[5])
            assert(amount <= len(stack[start]))  # assumption
            for i in range(amount):
                stack[end].append(stack[start].pop())
    answer = ''
    for i in range(1, len(stack)):
        answer += stack[i].pop()
    return answer


def part2(instructions, stack):
    for line in instructions:
        if 'move' in line:
            split = line.split(' ')
            amount = int(split[1])
            start = int(split[3])
            end = int(split[5])
            assert (amount <= len(stack[start]))  # assumption
            temp = []
            for i in range(amount):
                temp.append(stack[start].pop())
            for i in range(len(temp)):
                stack[end].append(temp.pop())
    answer = ''
    for i in range(1, len(stack)):
        answer += stack[i].pop()
    return answer


def create_stack(txt, n_lines, n_stacks):
    local_stack_of_crates = [[] for x in range(n_stacks + 1)]
    for line in range(n_lines):
        for i in range(1, len(txt[line]), 4):
            if txt[line][i] != ' ':
                local_stack_of_crates[i // 4 + 1].insert(0, (txt[line][i]))
    return local_stack_of_crates


if __name__ == '__main__':
    file = line_str(5)
    stack_of_crates = create_stack(file, 8, 9)
    test_file = line_str(5, True)
    test_stack_of_crates = create_stack(test_file, 3, 3)
    assert(part1(test_file, copy.deepcopy(test_stack_of_crates)) == 'CMZ')
    assert(part2(test_file, copy.deepcopy(test_stack_of_crates)) == 'MCD')
    print('part1:', part1(file, copy.deepcopy(stack_of_crates)))
    print('part2:', part2(file, copy.deepcopy(stack_of_crates)))
