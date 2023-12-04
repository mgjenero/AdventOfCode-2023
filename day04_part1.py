def parse_line(line):
    line = line.strip()
    card = line.split("|")
    winning_cards = card[0].split(":")[1].strip()
    cards = card[1].strip()

    return winning_cards, cards


def count_card_points(winning_cards, cards):
    winning_cards = set(winning_cards.split())
    cards = cards.split()
    points = 0
    for card in cards:
        if card in winning_cards:
            points = 1 if points == 0 else points * 2
    return points


def count_total_points(lines):
    total_points = 0
    for line in lines:
        winning_cards, cards = parse_line(line)
        total_points += count_card_points(winning_cards, cards)
    return total_points

# Testing


test1 = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]
ans1 = 13

assert count_total_points(test1) == ans1

# Read input
with open("day4.txt", "r") as f:
    lines = f.readlines()
    print(count_total_points(lines))

# Runtime = O(n*m)
# Space O(m)
#
# where n is the number of lines(equivalent to number of cards)
# where m is lenght of line
# m should be constant cause it's convenient for physical cards to have constant number
# of winning numbers and numbers you have, but here is included just in case
