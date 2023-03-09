def find_common_bit_value(list_of_bytes: list, bit_index: int) -> int:
    bits = ""
    for byte in list_of_bytes:
        bits += byte[bit_index]

    if bits.count('1') >= len(bits) / 2:
        return 1
    return 0


with open("input.txt") as file:
    oxygen_generator_rating_data = [num.strip() for num in file.readlines()]
    C02_scrubber_rating_data = oxygen_generator_rating_data[:]

    for i in range(len(oxygen_generator_rating_data[0])):
        if len(oxygen_generator_rating_data) == 1:
                break

        common_bit = find_common_bit_value(oxygen_generator_rating_data, i)
            
        for byte in oxygen_generator_rating_data[:]:
            if int(byte[i]) != common_bit:
                oxygen_generator_rating_data.remove(byte)


    for i in range(len(C02_scrubber_rating_data[0])):
        if len(C02_scrubber_rating_data) == 1:
                break
        uncommon_bit = 1 - find_common_bit_value(C02_scrubber_rating_data, i)

        for byte in C02_scrubber_rating_data[:]:
            if int(byte[i]) != uncommon_bit:
                C02_scrubber_rating_data.remove(byte)

oxygen_generator_rating = int(oxygen_generator_rating_data[0], 2)
C02_scrubber_rating = int(C02_scrubber_rating_data[0], 2)
print("part 2: ", oxygen_generator_rating * C02_scrubber_rating)
