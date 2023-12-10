grid = {}
numbers = []
input_file = open("input.txt", "r")
y_index = 0
for line in input_file:
    line = line.strip()
    x_index = 0
    x_axis = {}

    number = ''
    coords = []
    for char in line:
        # Add value to grid
        x_axis[x_index] = char
        # Add number into numbers list
        if char.isnumeric():
            number += str(char)
            coords.append((x_index, y_index))
        else:
            if len(number) > 0:
                numbers.append({'value': int(number), 'coords': coords})
            number = ''
            coords = []
        # Move on x index
        x_index += 1
    if len(number) > 0:
        numbers.append({'value': int(number), 'coords': coords})
    grid[y_index] = x_axis
    y_index += 1

input_file.close()


def char_surrounding(x, y):
    char_found = False
    coords_around = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                     (x - 1, y), (x + 1, y),
                     (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
    for coord in coords_around:
        value = None
        y_axis = grid.get(coord[1])
        if y_axis is not None:
            value = y_axis.get(coord[0])
        if value is not None and value != '.' and not value.isnumeric():
            char_found = True
    return char_found

total = 0
for number in numbers:
    char_found = False
    for coord in number['coords']:
        if char_surrounding(coord[0], coord[1]):
            char_found = True
    if char_found:
        total += number['value']

print(total)
