scratchcards = []
input_file = open("input.txt", "r")
for line in input_file:
    line = line.split(":")[1].strip().split("|")
    winning = line[0].strip().split()
    my_cards = line[1].strip().split()
    scratchcards.append((winning, my_cards))
input_file.close()

total = 0
for scratchcard in scratchcards:
    value = 0
    winning, my_cards = scratchcard
    for my_card in my_cards:
        if my_card in winning:
            if value == 0:
                value = 1
            else:
                value *= 2
    if value > 0.5:
        total += value

print(total)
