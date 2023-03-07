with open("input.txt") as input:
    measurements = [int(measurement.strip()) for measurement in input.readlines()]
    count_increases = 0
    current_measurement = measurements[0]
    for measurement in measurements:
        if measurement > current_measurement:
            count_increases += 1
        current_measurement = measurement
print(count_increases)
