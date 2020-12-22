def play_game(deck1, deck2):
    prev_rounds = []
    while deck1 and deck2:
        if (deck1, deck2) in prev_rounds:
            return ("player1", deck1)
        else:
            prev_rounds.append((deck1.copy(), deck2.copy()))
        card1, card2 = deck1.pop(0), deck2.pop(0)
        if len(deck1) >= card1 and len(deck2) >= card2:
            new_deck1, new_deck2 = deck1[:card1], deck2[:card2]
            winner, cards = play_game(new_deck1, new_deck2)
            if winner == "player1":
                deck1 += [card1, card2]
            else:
                deck2 += [card2, card1]
        else:
            if card1 > card2:
                deck1 += [card1, card2]
            elif card2 > card1:
                deck2 += [card2, card1]
    return ("player1", deck1) if deck1 else ("player2", deck2)


def calc_winner(deck):
    return sum([i * (idx + 1) for idx, i in enumerate(deck[::-1])])


def main():
    with open("22.txt") as input:
        lines = [line.strip() for line in input.readlines()]
        deck1 = [int(c) for c in lines[1 : (len(lines) // 2)]]
        deck2 = [int(c) for c in lines[len(lines) // 2 + 2 :]]
        winner, deck = play_game(deck1, deck2)
        print(calc_winner(deck))
    return 0


if __name__ == "__main__":
    exit(main())