class Round:
    SCORES = {
        "X": {
            "A": 4,  # 1 for rock plus 3 for draw
            "B": 1,  # 1 for rock plus 0 for loss
            "C": 7,  # 1 for rock plus 6 for win
        },
        "Y": {
            "A": 8,  # 2 for paper plus 6 for win
            "B": 5,  # 2 for paper plus 3 for draw
            "C": 2,  # 2 for paper plus 0 for loss
        },
        "Z": {
            "A": 3,  # 3 for scissors plus 0 for loss
            "B": 9,  # 3 for scissors plus 6 for win
            "C": 6,  # 3 for scissors plus 3 for draw
        },
    }

    def __init__(self, opponent_choice, self_choice):
        self._opponent_choice = opponent_choice
        self._self_choice = self_choice

    @property
    def opponent_choice(self):
        return self._opponent_choice

    @property
    def self_choice(self):
        return self._self_choice

    def score(self):
        return self.SCORES[self._self_choice][self._opponent_choice]


def parse_rounds(lines):
    return [Round(*line.strip().split()) for line in lines]
