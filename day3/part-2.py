numbers = []
potential_gears = []
input_file = open("input.txt", "r")
y_index = 0
for line in input_file:
    line = line.strip()
    x_index = 0

    number = ''
    coords = []
    for char in line:
        # Add number into numbers list
        if char.isnumeric():
            number += str(char)
            coords.append((x_index, y_index))
        else:
            if len(number) > 0:
                numbers.append({'value': int(number), 'coords': coords})
            if char == '*':
                potential_gears.append((x_index, y_index))
            number = ''
            coords = []
        # Move on x index
        x_index += 1
    if len(number) > 0:
        numbers.append({'value': int(number), 'coords': coords})
    y_index += 1

input_file.close()

def number_around(x, y, coords):
    coords_around = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                     (x - 1, y), (x + 1, y),
                     (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
    for coord in coords:
        if coord in coords_around:
            return True
    return False

def gear_value(x, y) :
    found_around = []
    for number in numbers:
        if number_around(x, y, number['coords']):
            found_around.append(number['value'])
    if len(found_around) == 2:
        return found_around[0] * found_around[1]
    return None

total = 0
for gear in potential_gears:
    gear_val = gear_value(gear[0], gear[1])
    if gear_val is not None:
        total += gear_val
print(total)
