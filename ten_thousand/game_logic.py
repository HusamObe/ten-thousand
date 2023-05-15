import random


class GameLogic:
    @staticmethod
    def roll_dice(num_dice):
        # Roll the dice and return the values as a tuple

        # Ensure the number of dice is between 1 and 6
        num_dice = max(1, min(6, num_dice))

        # Generate random values for each dice
        dice_roll = tuple(random.randint(1, 6) for _ in range(num_dice))

        return dice_roll

    @staticmethod
    def calculate_score(roll):
        # Calculate the score for the given dice roll

        # Score rules:
        # - A single 1 is worth 100 points
        # - A single 5 is worth 50 points
        # - Three of a kind (except for 1s) are worth 100 times the number (e.g., three 4s are worth 400 points)
        # - Three 1s are worth 1000 points
        # - Additional 1s in a three of a kind group are worth 100 points each
        # - Additional 5s in a three of a kind group are worth 50 points each

        score = 0

        # Count the occurrences of each number in the roll
        counts = [roll.count(i) for i in range(1, 7)]

        # Calculate the score based on the counts
        for number in range(1, 7):
            count = counts[number - 1]

            if count >= 3:
                if number == 1:
                    score += 1000
                else:
                    score += number * 100

                # Deduct the count of three from the original count
                count -= 3

                # Add additional points for extra 1s or 5s
                if number == 1:
                    score += count * 100
                elif number == 5:
                    score += count * 50

            # Add individual points for 1s and 5s
            if number == 1:
                score += count * 100
            elif number == 5:
                score += count * 50

            if sorted(roll) == [1, 2, 3, 4, 5, 6]:  # Straight 1-6
                score = 1500
            elif count == 4:  # Four of a kind
                score = 400
            elif count == 5:  # Five of a kind
                score = 600
            elif count == 6:  # Six of a kind
                score = 800
            elif roll == (1, 1, 1, 1, 1, 1):  # Six ones
                score = 4000
            elif roll == (2, 2, 2, 2):  # four of a kind of 2s
                score = 400
            elif roll == (3, 3, 3, 3):  # four of a kind of 3s
                score = 600
            elif roll == (4, 4, 4, 4):  # four of a kind of 4s
                score = 800
            elif roll == (5, 5, 5, 5):  # four of a kind of 5s
                score = 1000
            elif roll == (6, 6, 6, 6):  # four of a kind of 6s
                score = 1200
            elif roll == (2, 2, 2, 2, 2):  # five of a kind of 2s
                score = 600
            elif roll == (3, 3, 3, 3, 3):  # five of a kind of 3s
                score = 900
            elif roll == (4, 4, 4, 4, 4):  # five of a kind of 4s
                score = 1200
            elif roll == (5, 5, 5, 5, 5):  # five of a kind of 5s
                score = 1500
            elif roll == (6, 6, 6, 6, 6):  # five of a kind of 6s
                score = 1800
            elif roll == (2, 2, 2, 2, 2, 2):  # six of a kind of 2s
                score = 800
            elif roll == (3, 3, 3, 3, 3, 3):  # six of a kind of 3s
                score = 1200
            elif roll == (4, 4, 4, 4, 4, 4):  # six of a kind of 4s
                score = 1600
            elif roll == (5, 5, 5, 5, 5, 5):  # six of a kind of 5s
                score = 2000
            elif roll == (6, 6, 6, 6, 6, 6):  # six of a kind of 6s
                score = 2400

        return score


game = GameLogic.roll_dice(6)
score = GameLogic.calculate_score(game)
print(f"Dice Roll: {game}")
print(f"Score: {score}")
