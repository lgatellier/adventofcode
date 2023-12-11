from __future__ import annotations

CARD_NUMERIC_VALUES = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
}


class Card:
    def __init__(self, kind: str):
        if len(kind) != 1:
            raise ValueError(f"'{kind}' is not a value Card kind !")
        self.__kind = kind
        self.__value = (
            int(self.kind) if self.kind.isdigit() else CARD_NUMERIC_VALUES[self.kind]
        )

    @property
    def value(self):
        return self.__value

    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, Card) and __value.kind == self.kind

    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)

    def __gt__(self, __value: object) -> bool:
        if not isinstance(__value, Card):
            raise ValueError("Cannot compare Card with non-Card object !")
        return self.value > __value.value

    def __lt__(self, __value: object) -> bool:
        if not isinstance(__value, Card):
            raise ValueError("Cannot compare Card with non-Card object !")
        return self.value < __value.value

    def __ge__(self, __value: object) -> bool:
        return not self.__lt__(__value)

    def __le__(self, __value: object) -> bool:
        return not self.__gt__(__value)

    @property
    def kind(self):
        return self.__kind

    def __repr__(self) -> str:
        return self.kind


class Hand:
    def __init__(self, cards: list[Card], bid: int, j_is_joker: bool = False) -> None:
        self.cards = cards
        self.bid = bid
        self.numeric_value = 0
        # Compute hand numeric value for hands comparison
        for i in range(len(cards)):
            self.numeric_value += cards[i].value * (pow(14, len(cards) - i))
        self.type = HandType.parse(self, j_is_joker)

    def winnings(self, rank: int) -> int:
        return self.bid * rank

    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, Hand) and self.cards == __value.cards

    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)

    def __gt__(self, __value: object) -> bool:
        if not isinstance(__value, Hand):
            raise ValueError("Cannot compare Hand with non-Hand object !")
        if self.type > __value.type:
            return True
        return self.type == __value.type and self.numeric_value > __value.numeric_value

    def __lt__(self, __value: object) -> bool:
        if not isinstance(__value, Hand):
            raise ValueError("Cannot compare Hand with non-Hand object !")
        if self.type < __value.type:
            return True
        return self.type == __value.type and self.numeric_value < __value.numeric_value

    def __ge__(self, __value: object) -> bool:
        return not self.__lt__(__value)

    def __le__(self, __value: object) -> bool:
        return not self.__gt__(__value)


class HandType:
    TYPES_VALUES = {
        "FIVE_OF_A_KIND": 6,
        "FOUR_OF_A_KIND": 5,
        "FULL_HOUSE": 4,
        "THREE_OF_A_KIND": 3,
        "TWO_PAIRS": 2,
        "ONE_PAIR": 1,
        "HIGH_CARD": 0,
    }

    def __init__(self, type: str):
        if type not in self.TYPES_VALUES:
            raise ValueError(f"Unknown type '{type}'")
        self.__type = type
        self.__value = self.TYPES_VALUES[type]

    @property
    def value(self):
        return self.__value

    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, HandType) and __value.value == self.value

    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)

    def __gt__(self, __value: object) -> bool:
        if not isinstance(__value, HandType):
            raise ValueError("Cannot compare HandType with non-HandType object !")
        return self.value > __value.value

    def __lt__(self, __value: object) -> bool:
        if not isinstance(__value, HandType):
            raise ValueError("Cannot compare HandType with non-HandType object !")
        return self.value < __value.value

    def __ge__(self, __value: object) -> bool:
        return not self.__lt__(__value)

    def __le__(self, __value: object) -> bool:
        return not self.__gt__(__value)

    @staticmethod
    def parse(hand: Hand, j_is_joker: bool = False) -> HandType:
        kinds = {}
        for k in ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]:
            kinds[k] = 0
        for c in hand.cards:
            kinds[c.kind] = kinds[c.kind] + 1
        sorted_kinds = sorted(kinds.items(), key=lambda k: k[1], reverse=True)
        if j_is_joker and sorted_kinds[0][0] == "J":
            primary_index = 1
            secondary_index = 2
        elif j_is_joker and sorted_kinds[1][0] == "J":
            primary_index = 0
            secondary_index = 2
        else:
            primary_index = 0
            secondary_index = 1
        primary_kind_count = sorted_kinds[primary_index][1]
        if j_is_joker:
            primary_kind_count += kinds["J"]
        secondary_kind_count = sorted_kinds[secondary_index][1]
        if primary_kind_count == 5:
            return HandType("FIVE_OF_A_KIND")
        if primary_kind_count == 4:
            return HandType("FOUR_OF_A_KIND")
        if primary_kind_count == 3:
            if secondary_kind_count == 2:
                return HandType("FULL_HOUSE")
            return HandType("THREE_OF_A_KIND")
        if primary_kind_count == 2:
            if secondary_kind_count == 2:
                return HandType("TWO_PAIRS")
            return HandType("ONE_PAIR")
        return HandType("HIGH_CARD")


def parse_hand(line: str, j_is_joker: bool = False):
    split = line.split(" ")
    cards = [Card(c) for c in split[0]]
    bid = int(split[1])
    return Hand(cards, bid, j_is_joker)
