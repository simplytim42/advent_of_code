def calculate_points_in_line(start, end):
    x1, y1 = [int(coord) for coord in start.split(",")]
    x2, y2 = [int(coord) for coord in end.split(",")]
    list_of_coords = []

    if x1 == x2:
        # line is horizontal
        x = x1
        if y1 < y2:
            iterations = range(y1, y2+1)
        else:
            iterations = range(y2, y1+1)

        for y in iterations:
            list_of_coords.append(str(x) + "," + str(y))

        return list_of_coords

    if y1 == y2:
        # line is vertical
        y = y1
        if x1 < x2:
            iterations = range(x1, x2+1)
        else:
            iterations = range(x2, x1+1)

        for x in iterations:
            list_of_coords.append(str(x) + "," + str(y))
        
        return list_of_coords
    
    return []


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

print("part 1: ", total)