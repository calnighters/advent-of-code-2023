scratchcards = {}
input_file = open("input.txt", "r")
for line in input_file:
    line = line.replace("Card", "").strip()
    card_no = int(line.split(":")[0])
    line = line.split(":")[1].strip().split("|")
    winning = line[0].strip().split()
    my_cards = line[1].strip().split()
    scratchcards[card_no] = {'amount': 1, 'card': (winning, my_cards)}
input_file.close()


def winning_count(scratchcard):
    count_wins = 0
    winning, my_cards = scratchcard['card']
    for my_card in my_cards:
        if my_card in winning:
            count_wins += 1
    return count_wins

for id, scratchcard in scratchcards.items():
    for i in range(0, scratchcard['amount']):
        for i in range(1, winning_count(scratchcard) + 1):
            scratchcards[id+i]['amount'] += 1

total = 0
for id, scratchcard in scratchcards.items():
    total += scratchcard['amount']

print(total)


