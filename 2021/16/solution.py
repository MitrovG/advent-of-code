
with open('input.txt', 'r') as fin:
    data = fin.read()

binary_string = bin(int(data, 16))[2:].zfill(len(data) * 4)


def packets(binary_string: str, idx: int):

    packet_version = int(binary_string[idx: idx + 3], 2)
    idx += 3

    packet_type = int(binary_string[idx: idx + 3], 2)
    idx += 3

    if packet_type == 4:  # literal
        number_b = ''
        while True:
            prefix = binary_string[idx]
            number_b += binary_string[idx+1:idx+5]
            idx += 5
            if prefix == '0':
                return packet_version, int(number_b, 2), idx

    else:  # operator
        values = list()
        length_type = binary_string[idx]
        idx += 1
        if length_type == '0':
            number_bits = int(binary_string[idx:idx+15],2)
            idx += 15
            break_idx = idx + number_bits
            while True:
                version, value, new_idx = packets(binary_string, idx)
                packet_version += version
                values.append(value)
                idx = new_idx
                if new_idx >= break_idx:
                    break
        else:
            number_packets = int(binary_string[idx:idx+11], 2)
            idx += 11
            for _ in range(number_packets):
                version, value, new_idx = packets(binary_string, idx)
                packet_version += version
                values.append(value)
                idx = new_idx

        if packet_type == 0:
            return packet_version, sum(values), idx
        elif packet_type == 1:
            p = 1
            for v in values:
                p *= v
            return packet_version, p, idx
        elif packet_type == 2:
            return packet_version, min(values), idx
        elif packet_type == 3:
            return packet_version, max(values), idx
        elif packet_type == 5:
            return packet_version, 1 if values[0] > values[1] else 0, idx
        elif packet_type == 6:
            return packet_version, 1 if values[0] < values[1] else 0, idx
        elif packet_type == 7:
            return packet_version, 1 if values[0] == values[1] else 0, idx


solution = packets(binary_string, 0)
solution_1 = solution[0]
solution_2 = solution[1]

print(solution_1)
print(solution_2)

