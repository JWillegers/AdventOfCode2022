from readFile import *


def part1(sensors_and_beacons, interested_row):
    no_beacon_in_row = set()
    offset = 0

    # First check if there is already a sensor or beacon in our interested row that we need to account for
    for pair in sensors_and_beacons:
        if pair[0][1] == interested_row and pair[0] not in no_beacon_in_row:
            no_beacon_in_row.add(pair[0])
            offset += 1
        if pair[1][1] == interested_row and pair[1] not in no_beacon_in_row:
            no_beacon_in_row.add(pair[1])
            offset += 1

    # Loop over all sensors and beacons
    for pair in sensors_and_beacons:
        distance = pair[2]
        if pair[0][1] - distance <= interested_row <= pair[0][1] + distance:
            x_start = pair[0][0]
            x_offset = 0
            no_beacon_in_row.add((x_start, interested_row))
            while abs(x_start + x_offset - pair[0][0]) + abs(pair[0][1] - interested_row) < distance:
                x_offset += 1
                no_beacon_in_row.add((x_start + x_offset, interested_row))
                no_beacon_in_row.add((x_start - x_offset, interested_row))

    return len(no_beacon_in_row) - offset


def part2(sensors_and_beacons, max_row):
    for pair in sensors_and_beacons:
        t = True
        # TODO walk around 'the edge'
    return -1


def parse(f):
    sensor_beacon = set()
    for line in f:
        parts = line.split('=')
        sensor_x = int(parts[1].split(',')[0])
        sensor_y = int(parts[2].split(':')[0])
        beacon_x = int(parts[3].split(',')[0])
        beacon_y = int(parts[4])
        sensor_beacon.add(((sensor_x, sensor_y), (beacon_x, beacon_y), abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)))
    return sensor_beacon


if __name__ == '__main__':
    testFile = line_str(15, True)
    test_sensors_and_beacons = parse(testFile)
    assert(part1(test_sensors_and_beacons, 10))
    print(part2(test_sensors_and_beacons, 20))
    file = line_str(15)
    global_sensors_and_beacons = parse(file)
    print('part1:', part1(global_sensors_and_beacons, 2_000_000))
    exit(0)
    print('part2:', part2(global_sensors_and_beacons, 4_000_000))
