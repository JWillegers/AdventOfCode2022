from readFile import *
from copy import deepcopy


def part1(cubes_to_check):
    surface_area = 0
    visited = []
    while len(cubes_to_check) > 0:
        cube = cubes_to_check.pop()
        visited.append(cube)
        cubes_to_check, neighbors_to_check, open_sides = check_neighbors(cube, visited, cubes_to_check, [])
        surface_area += open_sides
        while len(neighbors_to_check) > 0:
            cube = neighbors_to_check.pop()
            visited.append(cube)
            cubes_to_check, ntc, open_sides = check_neighbors(cube, visited, cubes_to_check, neighbors_to_check)
            surface_area += open_sides
            neighbors_to_check = neighbors_to_check.union(ntc)

    return surface_area


def check_neighbors(cube, visited, cubes_to_check, ntc):
    new_neighbors_to_check = set()
    new_open_sides = 0
    for i in range(3):
        for d in [-1, 1]:
            nx = cube[0] + d if i == 0 else cube[0]
            ny = cube[1] + d if i == 1 else cube[1]
            nz = cube[2] + d if i == 2 else cube[2]
            nc = (nx, ny, nz)
            if nc in cubes_to_check:
                new_neighbors_to_check.add(nc)
                cubes_to_check.remove(nc)
            elif nc not in visited and nc not in ntc:
                new_open_sides += 1
    return cubes_to_check, new_neighbors_to_check, new_open_sides





def parse(f):
    cubes = set()
    for line in f:
        s = line.split(',')
        cubes.add((int(s[0]), int(s[1]), int(s[2])))
    return list(cubes)


if __name__ == '__main__':
    test_file = line_str(18, True)
    test_cubes = parse(test_file)
    assert(part1(test_cubes) == 64)
    file = line_str(18)
    global_cubes = parse(file)
    print('part1:', part1(deepcopy(global_cubes)))  #7701 too high
