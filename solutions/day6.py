from readFile import *


def solution(datastream, n_distinct_characters):
    for i in range(n_distinct_characters + 1, len(datastream)):
       if len(set(datastream[i-n_distinct_characters:i])) == n_distinct_characters:
           return i
    return 'Nothing found'


def part2(datastream):
    for i in range(3, len(datastream)):
        if len(set(datastream[i - 3:i + 1])) == 4:
            return i + 1
    return 'Nothing found'


if __name__ == '__main__':
    file = line_str(6)
    print('part1:', solution(file[0], 4))
    print('part2:', solution(file[0], 14))
