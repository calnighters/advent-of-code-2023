lines= []
input_file = open("input.txt", "r")
for line in input_file:
    lines.append(line.strip())
input_file.close()

total = 0
for line in lines:
    numbers = []
    for val in line:
        if val.isnumeric():
            numbers.append(str(val))
    number = numbers[0] + numbers[-1]
    total += int(number)

print(total)