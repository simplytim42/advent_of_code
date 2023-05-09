with open("input.txt") as input:
    numbers = [int(numbers) for numbers in input.readlines()]
    for index in range(len(numbers)):
        number_a = numbers[index]
        for i, number in enumerate(numbers):
            if i == index:
                continue
            if number_a + number == 2020:
                print("part 1 answer: ", number_a * number)
                exit()
