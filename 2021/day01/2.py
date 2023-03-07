with open("input.txt") as input:
    measurements = [int(measurement.strip()) for measurement in input.readlines()]
    sum_of_three_measurements = []
    for i in range(len(measurements)):
        sum = measurements[i] + measurements[i+1] + measurements[i+2]
        sum_of_three_measurements.append(sum)
        if i == len(measurements) - 3: break

count_increases = 0
current_measurement = sum_of_three_measurements[0]
for measurement in sum_of_three_measurements:
    if measurement > current_measurement:
        count_increases += 1
    current_measurement = measurement
print(count_increases)