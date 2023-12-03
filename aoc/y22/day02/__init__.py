class Round:
    SCORES = {
        "A": {  # rock
            "X": 4,  # rock +1, +3 for draw
            "Y": 8,  # paper +2, +6 for win
            "Z": 3,  # scissors +3, + 0 for loss
        },
        "B": {  # paper
            "X": 1,  # rock +1, +0 for loss
            "Y": 5,  # paper +2, +3 for draw
            "Z": 9,  # scissors +3, +6 for win
        },
        "C": {  # scissors
            "X": 7,  # rock +1, +6 for win
            "Y": 2,  # paper +2, +0 for loss
            "Z": 6,  # scissors +3, +3 for draw
        },
    }

    def __init__(self, opponent_choice):
        self._opponent_choice = opponent_choice
        self._self_choice = None

    @property
    def opponent_choice(self):
        return self._opponent_choice

    @property
    def self_choice(self):
        return self._self_choice

    def score(self):
        return self.SCORES[self._opponent_choice][self._self_choice]


def parse_rounds(lines, cls):
    return [cls(*line.strip().split()) for line in lines]
