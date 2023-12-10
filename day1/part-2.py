lines= []
input_file = open("input.txt", "r")
for line in input_file:
    lines.append(line.strip())
input_file.close()

number_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

total = 0
for line in lines:
    numbers = []
    for i in range(0, len(line)):
        if line[i].isnumeric():
            numbers.append(str(line[i]))
        else:
            for num in number_map:
                if line[i:len(line)].startswith(num):
                    numbers.append(number_map[num])
    number = numbers[0] + numbers[-1]
    total += int(number)

print(total)


