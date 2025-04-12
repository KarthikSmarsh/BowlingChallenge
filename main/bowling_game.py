class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins: int):
        self.rolls.append(pins)

    def score(self) -> int:
        total_score = 0
        roll_index = 0

        for frame in range(10):
            if self.is_strike(roll_index):
                total_score += 10 + self.strike_bonus(roll_index)
                roll_index += 1
            elif self.is_spare(roll_index):
                total_score += 10 + self.spare_bonus(roll_index)
                roll_index += 2
            else:
                total_score += self.sum_frame(roll_index)
                roll_index += 2

        return total_score

    def is_strike(self, roll_index: int) -> bool:
        return self.rolls[roll_index] == 10

    def is_spare(self, roll_index: int) -> bool:
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10

    def strike_bonus(self, roll_index: int) -> int:
        return self.rolls[roll_index + 1] + self.rolls[roll_index + 2]

    def spare_bonus(self, roll_index: int) -> int:
        return self.rolls[roll_index + 2]

    def sum_frame(self, roll_index: int) -> int:
        return self.rolls[roll_index] + self.rolls[roll_index + 1]