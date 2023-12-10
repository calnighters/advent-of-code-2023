records = []
input_file = open("input.txt", "r")
for line in input_file:
    split_colon = line.strip().replace("Game ", "").split(":")
    split_semicolon = split_colon[1].split(";")
    record = {
        "id": int(split_colon[0]),
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for hand in split_semicolon:
        for type in hand.split(","):
            split_type = type.strip().split(" ")
            value = int(split_type[0])
            if value > record[split_type[1]]:
                record[split_type[1]] = value
    records.append(record)
input_file.close()

types = ["red", "green", "blue"]

total = 0
for record in records:
    power = 1
    for type in types:
        power *= record[type]
    total += power

print("total", total)