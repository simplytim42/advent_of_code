with open("input.txt") as input:
    numbers = [int(numbers) for numbers in input.readlines()]

    for index1 in range(len(numbers)):
        number_a = numbers[index1]

        for index2, number in enumerate(numbers):
            if index2 == index1:
                continue
            number_b = number

            for index3, number in enumerate(numbers):
                if index3 == index2:
                    continue

                if number_a + number_b + number == 2020:
                    print("part 2 answer: ", number_a * number_b * number)
                    exit()
