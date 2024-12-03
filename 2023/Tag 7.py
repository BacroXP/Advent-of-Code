import sys
import re
from collections import Counter


def process_hand(hand, use_variant):
    hand = hand.replace('T', chr(ord('9') + 1))
    hand = hand.replace('J', chr(ord('2') - 1) if use_variant else chr(ord('9') + 2))
    hand = hand.replace('Q', chr(ord('9') + 3))
    hand = hand.replace('K', chr(ord('9') + 4))
    hand = hand.replace('A', chr(ord('9') + 5))

    card_counts = Counter(hand)

    if use_variant:
        target_card = list(card_counts.keys())[0]
        for card in card_counts:
            if card != '1':
                if card_counts[card] > card_counts[target_card] or target_card == '1':
                    target_card = card
        assert target_card != '1' or list(card_counts.keys()) == ['1']
        if '1' in card_counts and target_card != '1':
            card_counts[target_card] += card_counts['1']
            del card_counts['1']
        assert '1' not in card_counts or list(card_counts.keys()) == ['1'], f'{card_counts} {hand}'

    if sorted(card_counts.values()) == [5]:
        return (10, hand)
    
    elif sorted(card_counts.values()) == [1, 4]:
        return (9, hand)
    
    elif sorted(card_counts.values()) == [2, 3]:
        return (8, hand)
    
    elif sorted(card_counts.values()) == [1, 1, 3]:
        return (7, hand)
    
    elif sorted(card_counts.values()) == [1, 2, 2]:
        return (6, hand)
    
    elif sorted(card_counts.values()) == [1, 1, 1, 2]:
        return (5, hand)
    
    elif sorted(card_counts.values()) == [1, 1, 1, 1, 1]:
        return (4, hand)
    
    else:
        assert False, f'{card_counts} {hand} {sorted(card_counts.values())}'


def main():
    file_path = "input.txt"

    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n')

    for use_variant in [False, True]:
        hands_and_bids = []

        for line in lines:
            hand, bid = line.split()
            hands_and_bids.append((hand, bid))

        sorted_hands = sorted(hands_and_bids, key=lambda hb: process_hand(hb[0], use_variant))

        total_score = 0

        for i, (hand, bid) in enumerate(sorted_hands):
            total_score += (i + 1) * int(bid)

        print(f'Total score for variant {use_variant}: {total_score}')


if __name__ == "__main__":
    main()
