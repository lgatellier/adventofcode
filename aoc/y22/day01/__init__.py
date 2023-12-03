class ElfCalories:
    def __init__(self):
        self._calories = []
        self._total = 0

    @property
    def total(self):
        return self._total

    @property
    def calories(self):
        return self._calories

    def add(self, value):
        self._calories.append(value)
        self._total += value

    def __repr__(self):
        return f"ElfCalories({self._total})"
