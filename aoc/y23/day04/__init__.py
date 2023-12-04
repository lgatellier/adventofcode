class Card:
    def __init__(
        self, card_number: int, winning_numbers: list[int], my_numbers: list[int]
    ):
        self.card_number = card_number
        self.winning_numbers = winning_numbers
        self.my_numbers = my_numbers

    @property
    def my_winning_numbers(self) -> list[int]:
        return list(set(self.winning_numbers) & set(self.my_numbers))


def parse_cards(lines: list[str]) -> list[Card]:
    return [parse_card(line) for line in lines]


def parse_card(line: str) -> Card:
    line_split = line.split(":")
    card_number = int(line_split[0][-3:])
    numbers = line.split(":")[1].split("|")
    winning_numbers = [int(n.strip()) for n in numbers[0].split(" ") if n != ""]
    my_numbers = [int(n.strip()) for n in numbers[1].split(" ") if n.strip() != ""]
    return Card(card_number, winning_numbers, my_numbers)


def parse_cards_grouped_by_number(lines: list[str]) -> dict[int, list[Card]]:
    cards = {}
    for line in lines:
        card = parse_card(line)
        cards[card.card_number] = [card]
    return cards
