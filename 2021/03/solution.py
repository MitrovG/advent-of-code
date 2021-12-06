
with open('input.txt', 'r') as fin:
    data = fin.read().split('\n')

counter = [0] * len(data[0])
for binary in data:
    for idx, value in enumerate(binary):
        value = int(value)
        counter[idx] += 1 if value == 1 else -1

gamma = int(''.join(['1' if element > 0 else '0' for element in counter]), 2)
epsilon = int(''.join(['0' if element > 0 else '1' for element in counter]), 2)

solution_1 = gamma * epsilon

##################################################################################

binary_length = len(data[0])

oxygen = list(data)
carbon = list(data)

for idx in range(binary_length):
    oxygen_bit = sum([1 if binary[idx] == '1' else -1 for binary in oxygen])
    oxygen_bit = '1' if oxygen_bit >= 0 else '0'
    carbon_bit = sum([1 if binary[idx] == '1' else -1 for binary in carbon])
    carbon_bit = '0' if carbon_bit >= 0 else '1'
    if len(oxygen) > 1:
        oxygen = [oxygen_element for oxygen_element in oxygen if oxygen_element[idx] == oxygen_bit]
    if len(carbon) > 1:
        carbon = [carbon_element for carbon_element in carbon if carbon_element[idx] == carbon_bit]

solution_2 = int(oxygen[0], 2) * int(carbon[0], 2)

############################################################################################################

print(solution_1)
print(solution_2)
