from functools import cmp_to_key

ranked_bits = {'A': 14,
               'K': 13,
               'Q': 12,
               'J': 11,
               'T': 10,
               '9': 9,
               '8': 8,
               '7': 7,
               '6': 6,
               '5': 5,
               '4': 4,
               '3': 3,
               '2': 2}
hands = []
input_file = open("input.txt", "r")
for line in input_file:
    line = line.strip().split()
    hands.append((line[0], int(line[1])))
input_file.close()


def split_hand(hand):
    split_hand = {}
    for char in hand:
        if char not in split_hand:
            split_hand[char] = 1
        else:
            split_hand[char] += 1
    return split_hand


def is_five_of_kind(hand):
    return len(hand) == 1


def is_four_of_kind(hand):
    return len(hand) == 2 and 4 in hand.values()


def is_full_house(hand):
    return len(hand) == 2 and 3 in hand.values()


def is_three_of_house(hand):
    return len(hand) == 3 and 3 in hand.values()


def is_two_pair(hand):
    return len(hand) == 3 and 2 in hand.values()


def is_one_pair(hand):
    return len(hand) == 4


def is_high_card(hand):
    return len(hand) == 5

five = []
four = []
full = []
three = []
two = []
one = []
high = []

for hand, bid in hands:
    split = split_hand(hand)
    if is_five_of_kind(split):
        five.append((hand, bid))
    elif is_four_of_kind(split):
        four.append((hand, bid))
    elif is_full_house(split):
        full.append((hand, bid))
    elif is_three_of_house(split):
        three.append((hand, bid))
    elif is_two_pair(split):
        two.append((hand, bid))
    elif is_one_pair(split):
        one.append((hand, bid))
    else:
        high.append((hand, bid))

def get_score(hand):
    score = 0
    hand_int_list = [ranked_bits.get(char) for char in hand]
    for i, number in enumerate(hand_int_list):
        # gives a big number to create a score to compare
        score += (10**(12-2*i)) * number
    return score

def compare_hands(hand_1, hand_2):
    hand_1_score = get_score(hand_1[0])
    hand_2_score = get_score(hand_2[0])
    return (hand_1_score > hand_2_score) - (hand_1_score < hand_2_score)

sorted_five = sorted(five, key=cmp_to_key(compare_hands))
sorted_four = sorted(four, key=cmp_to_key(compare_hands))
sorted_full = sorted(full, key=cmp_to_key(compare_hands))
sorted_three = sorted(three, key=cmp_to_key(compare_hands))
sorted_two = sorted(two, key=cmp_to_key(compare_hands))
sorted_one = sorted(one, key=cmp_to_key(compare_hands))
sorted_high = sorted(high, key=cmp_to_key(compare_hands))

sorted_hands = sorted_high
sorted_hands.extend(sorted_one)
sorted_hands.extend(sorted_two)
sorted_hands.extend(sorted_three)
sorted_hands.extend(sorted_full)
sorted_hands.extend(sorted_four)
sorted_hands.extend(sorted_five)

total = 0

for i, hand in enumerate(sorted_hands):
    total += ((i + 1) * hand[1])

print(total)