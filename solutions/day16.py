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
    steps_from_a_to_b = get_paths(data, valves_that_we_want_open)

    # assumption that I make, if False the code will break
    assert(data['AA']['flow'] == 0)
    valves_that_we_want_open.remove('AA')
    valves_that_we_want_open = list(valves_that_we_want_open)

    # greedy solution
    #greedy = sorted(valves_that_we_want_open, key=lambda x:data[x]['flow'], reverse=True)
    greedy = ['DD', 'BB', 'JJ', 'HH', 'EE', 'CC']
    greedy.insert(0, 'AA')
    max_score = calculate_score(data, greedy, steps_from_a_to_b)

    return max_score


def calculate_score(data, route, steps_from_a_to_b):
    time = 0
    index = 0
    fpm = 0
    total_flow = 0
    while time <= 30 and index + 1 < len(route):
        start = route[index]
        end = route[index + 1]
        # + 1 because we also need to open the valve
        time_needed_to_travel_and_open_valve = steps_from_a_to_b[(start, end)] + 1
        total_flow += fpm * min(30 - time, time_needed_to_travel_and_open_valve)
        time += time_needed_to_travel_and_open_valve
        fpm += data[route[index + 1]]['flow']
        index += 1

    if time <= 30:
        total_flow += fpm * (30 - time)

    return total_flow


def get_paths(data, valves_that_we_want_open):
    paths = dict()
    for x, y in itertools.combinations(valves_that_we_want_open, 2):
        paths[(x, y)] = len(find_path(x, y, data))
        paths[(y, x)] = len(find_path(y, x, data))
    return paths


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
    exit(0)
    file = line_str(16)
    global_tunnels = parse(file)
    print('part1:', part1(global_tunnels))
