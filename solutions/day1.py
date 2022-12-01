import copy

from readFile import *


def partA(list_of_elves):
    maximum = 0
    for elf in list_of_elves:
        maximum = max(maximum, sum(elf))
    return maximum


def partB(list_of_elves):
    maximum = []
    for elf in list_of_elves:
        maximum.append(sum(elf))
        maximum.sort(reverse=True)
        if len(maximum) > 3:
            del maximum[-1]
    return sum(maximum)


if __name__ == '__main__':
    file = line_str(1)
    elves = []
    calories = []
    for line in file:
        if len(line) == 0:
            elves.append(copy.deepcopy(calories))
            calories.clear()
        else:
            calories.append(int(line))
    print('part A:', partA(elves))
    print('part B:', partB(elves))
