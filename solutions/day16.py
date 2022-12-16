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
    paths = dict()
    for x, y in itertools.combinations(valves_that_we_want_open, 2):
        paths[(x, y)] = find_path(x, y, data)
        paths[(y, x)] = find_path(y, x, data)

    # assumption that I make, if False the code will break
    assert(data['AA']['flow'] == 0)
    valves_that_we_want_open.remove('AA')

    # (Location, time, flow per minute, total flow, opened_valves as [])
    queue = []
    for valve in valves_that_we_want_open:
        queue.append((valve, len(paths[('AA', valve)]), 0, 0, []))

    max_flow = 0
    while len(queue) > 0:
        location, time, fpm, total_flow, opened_valves = queue.pop(0)
        if time >= 30:
            old_max_flow = max_flow
            max_flow = max(max_flow, total_flow)
            if max_flow > old_max_flow:
                print(max_flow, opened_valves)
        else:
            total_flow += fpm
            time += 1
            fpm += data[location]['flow']
            ov_copy = deepcopy(opened_valves)
            ov_copy.append(location)
            dead_end = True
            for valve in valves_that_we_want_open:
                if valve not in ov_copy:
                    dead_end = False
                    time_jump = len(paths[(location, valve)])
                    new_total_flow = total_flow + min(time_jump, 30 - time) * fpm
                    queue.append((valve, time + time_jump,
                                  fpm, new_total_flow, ov_copy))
            if dead_end:
                old_max_flow = max_flow
                max_flow = max(max_flow, total_flow + (30 - time) * fpm)
                if max_flow > old_max_flow:
                    print(max_flow, opened_valves)

    return max_flow


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
    file = line_str(16)
    global_tunnels = parse(file)
    print('part1:', part1(global_tunnels))
