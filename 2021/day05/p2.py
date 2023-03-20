def calculate_points_in_line(start, end):
    x1, y1 = [int(coord) for coord in start.split(",")]
    x2, y2 = [int(coord) for coord in end.split(",")]
    list_of_coords = []

    # line is horizontal
    if x1 == x2:
        x = x1
        if y1 < y2:
            iterations = range(y1, y2+1)
        else:
            iterations = range(y2, y1+1)

        for y in iterations:
            list_of_coords.append(str(x) + "," + str(y))

        return list_of_coords

    # line is vertical
    if y1 == y2:
        y = y1
        if x1 < x2:
            iterations = range(x1, x2+1)
        else:
            iterations = range(x2, x1+1)

        for x in iterations:
            list_of_coords.append(str(x) + "," + str(y))
        
        return list_of_coords
    
    # line is diagonal
    iterations = abs(x1-x2)
    x = x1
    y = y1
    list_of_coords.append(str(x) + "," + str(y))
    for i in range(iterations):
        # calculate x
        if x > x2:
            x = x-1
        if x < x2:
            x = x+1
        # calculate y
        if y > y2:
            y = y-1
        if y < y2:
            y = y+1

        list_of_coords.append(str(x) + "," + str(y))
    return list_of_coords


coords_tally = {}
with open("input.txt") as file:
    for input in file.readlines():
        start, end = input.split("->")

        points = calculate_points_in_line(start, end)
        for point in points:
            if point in coords_tally:
                coords_tally[point] += 1
            else:
                coords_tally[point] = 1

total = 0
for coord, amount in coords_tally.items():
    if amount > 1:
        total+=1

print("part 2: ", total)