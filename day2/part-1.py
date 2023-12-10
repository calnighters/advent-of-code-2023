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

max_recs = {
    "red": 12,
    "green": 13,
    "blue": 14
}

total = 0
for record in records:
    possible = True
    for rec in max_recs:
        if record[rec] > max_recs[rec]:
            possible = False
    if possible:
        total += record["id"]

print("total", total)