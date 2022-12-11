import math
import re
from readFile import *


def part1(monkey_items, monkey_data, needed_rounds, factor_3):
    inspections = [0 for monkey in range(8)]
    for throw_round in range(needed_rounds):
        for index in range(len(monkey_data)):
            monkey = monkey_data[index]
            # Structure of if-statements only works because 'Operation: new = old + old' doesn't exists
            if monkey[1]:
                monkey_items, inspections = monkey_factor(monkey_items, inspections, index, monkey[3], monkey[4], monkey[5], factor_3)
            elif monkey[0]:
                monkey_items, inspections = monkey_multiplication(monkey_items, inspections, index, monkey[2], monkey[3], monkey[4], monkey[5], factor_3)
            else:
                monkey_items, inspections = monkey_addition(monkey_items, inspections, index, monkey[2], monkey[3], monkey[4], monkey[5], factor_3)
    highest_value = max(inspections)
    inspections.remove(highest_value)
    return highest_value * max(inspections)


def monkey_factor(monkey_items, inspections, monkey_index, test, monkey_true, monkey_false, factor_3):
    while len(monkey_items[monkey_index]) > 0:
        inspections[monkey_index] += 1
        old = monkey_items[monkey_index].pop(0)
        if factor_3:
            item = math.floor((old * old) / 3)
        else:
            item = old * old
        if item % test == 0:
            monkey_items[monkey_true].append(item)
        else:
            monkey_items[monkey_false].append(item)
    return monkey_items, inspections


def monkey_multiplication(monkey_items, inspections, monkey_index, factor, test, monkey_true, monkey_false, factor_3):
    while len(monkey_items[monkey_index]) > 0:
        inspections[monkey_index] += 1
        if factor_3:
            item = math.floor((monkey_items[monkey_index].pop(0) * factor) / 3)
        else:
            item = monkey_items[monkey_index].pop(0) * factor
        if item % test == 0:
            monkey_items[monkey_true].append(item)
        else:
            monkey_items[monkey_false].append(item)
    return monkey_items, inspections


def monkey_addition(monkey_items, inspections, monkey_index, add, test, monkey_true, monkey_false, factor_3):
    while len(monkey_items[monkey_index]) > 0:
        inspections[monkey_index] += 1
        if factor_3:
            item = math.floor((monkey_items[monkey_index].pop(0) + add) / 3)
        else:
            item = monkey_items[monkey_index].pop(0) + add
        if item % test == 0:
            monkey_items[monkey_true].append(item)
        else:
            monkey_items[monkey_false].append(item)
    return monkey_items, inspections


if __name__ == '__main__':
    file = line_str(11)
    global_monkey_items = []
    ''''
    global_monkey_data structure:
    [
    multiplication: bool
    self: bool
    operation value: int
    test value: int
    throw true: int
    throws false: int
    ]
    '''
    global_monkey_data = [[] for monkey in range(4)]
    for i in range(1, len(file)):
        global_index = i // 7
        line = file[i]
        if i % 7 == 1:
            # starting items
            numbers = line.split(':')[1][1:].split(', ')
            m = []
            for j in numbers:
                m.append(int(j))
            global_monkey_items.append(m)
        elif i % 7 == 2:
            # operation
            global_monkey_data[global_index].append('*' in line)
            global_monkey_data[global_index].append(not bool(re.search(r'\d', line)))  # check digit in string
            if not global_monkey_data[global_index][0] and global_monkey_data[global_index][1]:
                print('\'Operation: new = old + old\' is not supported')
                exit(0)
            if global_monkey_data[global_index][1]:
                global_monkey_data[global_index].append(None)
            else:
                global_monkey_data[global_index].append(int(line.split(' ')[-1]))
        elif 0 < i % 7 < 6:
            # test, if true, if false
            global_monkey_data[global_index].append(int(line.split(' ')[-1]))

    print('part1:', part1(global_monkey_items, global_monkey_data, 20, True))
    print('part2:', part1(global_monkey_items, global_monkey_data, 10000, False))
