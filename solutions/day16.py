import math
from readFile import *
from copy import deepcopy
import itertools


def part1(data):
    # find all valves with flow > 0
    valves_that_we_want_open = set()
    for valve in data.keys():
        if data[valve]['flow'] > 0:
            valves_that_we_want_open.add(valve)

    # key is as follows (start, goal)
    valves_that_we_want_open.add('AA')
    paths = get_paths(data, valves_that_we_want_open)

    # assumption that I make, if False the code will break
    assert(data['AA']['flow'] == 0)
    valves_that_we_want_open.remove('AA')
    valves_that_we_want_open = list(valves_that_we_want_open)

    # (Location, time, flow per minute, total flow, opened_valves as [])
    queue = [('AA', 0, 0, 0, [])]

    max_flow = 0
    while len(queue) > 0:
        location, time, fpm, total_flow, opened_valves = queue.pop()
        max_flow, queue = process(queue, data, valves_that_we_want_open, paths, max_flow, location, time, fpm, total_flow, opened_valves)
    print(max_flow)
    return max_flow


def get_paths(data, valves_that_we_want_open):
    paths = dict()
    for x, y in itertools.combinations(valves_that_we_want_open, 2):
        paths[(x, y)] = find_path(x, y, data)
        paths[(y, x)] = find_path(y, x, data)
    return paths


def process(queue, data, valves_that_we_want_open, paths, max_flow, location, time, fpm, total_flow, opened_valves):
    if time >= 30:
        max_flow = max(max_flow, total_flow)
    expected_new_flow = []
    for valve in valves_that_we_want_open:
        if valve is not location and valve not in opened_valves:
            expected_new_flow.append((valve, (30 - time - len(paths[(location, valve)]) - 1) * data[valve]['flow']))
    expected_new_flow = sorted(expected_new_flow, key=lambda x: x[1], reverse=True)
    if len(expected_new_flow) == 0:
        max_flow = max(max_flow, total_flow + (30 - time) * (fpm + data[location]['flow']))
    else:
        for i in range(min(1 + math.ceil(len(valves_that_we_want_open) / 3), len(expected_new_flow))):
            valve = expected_new_flow[i][0]
            new_fpm = fpm + data[location]['flow']
            cov = deepcopy(opened_valves)
            cov.append(valve)
            queue.append((valve, time + len(paths[(location, valve)]) + 1, new_fpm,
                          total_flow + min(30 - time, len(paths[(location, valve)]) + 1) * new_fpm, cov))
    return max_flow, queue



# BFS
def find_path(start, goal, data):
    visited = [start]
    queue = [[start]]
    while len(queue) > 0:
        path = queue.pop(0)
        last_location = path[-1]
        for neighbor in data[last_location]['tunnels']:
            if neighbor == goal:
                path.append(goal)
                path.remove(start)  # since we start at start, we don't have to move their anymore
                return path
            if neighbor not in visited:
                path_copy = deepcopy(path)
                path_copy.append(neighbor)
                visited.append(neighbor)
                queue.append(path_copy)
    print('ERROR: PATH NOT FOUND')
    exit(1)


def parse(data):
    parts = dict()
    for line in data:
        split = line.split(' ')
        parts[split[1]] = dict()
        parts[split[1]]['flow'] = int(split[4].split('=')[1].replace(';', ''))
        parts[split[1]]['tunnels'] = []
        for i in range(9, len(split)):
            parts[split[1]]['tunnels'].append(split[i].replace(',', ''))
    return parts


if __name__ == '__main__':
    test_file = line_str(16, True)
    test_tunnels = parse(test_file)
    assert(part1(test_tunnels) == 1651)
    #exit(0)
    file = line_str(16)
    global_tunnels = parse(file)
    print('part1:', part1(global_tunnels))
