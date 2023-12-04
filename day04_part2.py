def parse_line(line):
    line = line.strip()
    card = line.split("|")
    game_id = int(card[0].split(":")[0].split()[1].strip())
    winning_cards = card[0].split(":")[1].strip()
    cards = card[1].strip()

    return game_id, winning_cards, cards


def matching_number_count(winning_cards, cards):
    winning_cards = winning_cards.split()
    cards = cards.split()
    total = 0
    for card in cards:
        if card in winning_cards:
            total += 1
    return total


def count_total_cards(lines):
    total_cards = 0
    added_cards = {}
    max_game_id = len(lines)

    for line in lines:
        game_id, winning_cards, cards = parse_line(line)
        matching_numbers = matching_number_count(winning_cards, cards)
        current_card_count = 1 + added_cards.get(game_id, 0)
        total_cards += current_card_count

        if matching_numbers > 0:
            upper_limit = min(matching_numbers, max_game_id - game_id)
            for i in range(1, upper_limit + 1):
                added_cards[game_id +
                            i] = added_cards.get(game_id + i, 0) + current_card_count
    return total_cards

# Testing


test1 = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]
ans1 = 30

assert count_total_cards(test1) == ans1

# Read input
with open("day4.txt", "r") as f:
    lines = f.readlines()
    print(count_total_cards(lines))

# Runtime = O(n^2*m)
# Explanation:we have additional for loop which can iterate for min(n, matching_numbers) times
# but for n >> m we can just say O(n*m)
# Space O(n+m)
# Explanation: also can be simplified to O(n) if n >> m
