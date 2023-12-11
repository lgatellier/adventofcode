from aoc.y23.day07 import Card, HandType, parse_hand


def test_card():
    cardA = Card("A")
    cardT = Card("T")
    assert cardA > cardT
    assert cardA != cardT
    cardA = Card("A")
    cardK = Card("K")
    assert cardA > cardK
    assert cardA >= cardK
    assert cardK < cardA
    assert cardK <= cardA
    assert cardA != cardK
    cardA1 = Card("A")
    cardA2 = Card("A")
    assert cardA1 == cardA2


def test_parse_hand():
    hand = parse_hand("32555 626")
    assert len(hand.cards) == 5
    assert hand.cards[0] == Card("3")
    assert hand.cards[1] == Card("2")
    assert hand.cards[2] == Card("5")
    assert hand.cards[3] == Card("5")
    assert hand.cards[4] == Card("5")
    assert hand.bid == 626


def test_hand_numeric_value():
    hand = parse_hand("32555 626")
    assert hand.numeric_value == 1705074
    hand = parse_hand("3A555 626")
    assert hand.numeric_value == 2166066
    hand = parse_hand("44555 626")
    assert hand.numeric_value == 2319730
    hand = parse_hand("44556 626")
    assert hand.numeric_value == 2319744


def test_hands_types():
    hand = parse_hand("32495 626")
    assert hand.type == HandType("HIGH_CARD")
    hand = parse_hand("32455 626")
    assert hand.type == HandType("ONE_PAIR")
    hand = parse_hand("52425 626")
    assert hand.type == HandType("TWO_PAIRS")
    hand = parse_hand("32555 626")
    assert hand.type == HandType("THREE_OF_A_KIND")
    hand = parse_hand("44555 626")
    assert hand.type == HandType("FULL_HOUSE")
    hand = parse_hand("44445 626")
    assert hand.type == HandType("FOUR_OF_A_KIND")
    hand = parse_hand("44444 626")
    assert hand.type == HandType("FIVE_OF_A_KIND")
    hand = parse_hand("4444J 626", False)
    assert hand.type == HandType("FOUR_OF_A_KIND")
    hand = parse_hand("4444J 626", True)
    assert hand.type == HandType("FIVE_OF_A_KIND")
