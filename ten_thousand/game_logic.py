import random


class GameLogic:
    @staticmethod
    def roll_dice(num_dice):
        if num_dice < 1 or num_dice > 6:
            raise ValueError("Number of dice must be between 1 and 6.")

        values = tuple(random.randint(1, 6) for _ in range(num_dice))
        return values

    @staticmethod
    def calculate_score(dice):
        score = 0
        counts = [0] * 7

        for die in dice:
            counts[die] += 1

        # for the 3 pairs HOT DICE
        if counts[1] != 2 and sum(count == 2 for count in counts[2:]) == 3:
            score = 1500
            return score

        # for the triple ones and above
        if counts[1] >= 3:
            score += 1000 * (counts[1] - 2)
            counts[1] = 0

        for i in range(2, 7):
            if counts[i] >= 3:
                score += i * 100 * (counts[i] - 2)
                counts[i] = 0

        if set(dice) == set([1, 2, 3, 4, 5, 6]):
            score = 1500
        elif set(counts[2:]) == {2} and counts[1] == 0:
            score = 1500
        elif (
            all(count in {2, 3, 4, 5, 6} for count in counts[1:])
            and len(set(counts[1:])) == 1
        ):
            score = 3000
        else:
            score += counts[1] * 100
            score += counts[5] * 50

        return score

    def play(self):
        print("Welcome to Ten Thousand")
        choice = input("(y)es to play or (n)o to decline\n> ")

        if choice.lower() != "y":
            print("OK. Maybe another time")
            return

        total_score = 0
        round_num = 1

        while True:
            print(f"Starting round {round_num}")
            round_score = 0
            num_dice = 6

            while True:
                print(f"Rolling {num_dice} dice...")
                dice = self.roll_dice(num_dice)
                print("***", " ".join(str(d) for d in dice), "***")

                keep = input("Enter dice to keep, or (q)uit:\n> ")

                if keep.lower() == "q":
                    print(f"Thanks for playing. You earned {total_score} points")
                    return

                try:
                    keep_values = [int(value) for value in keep.split()]
                    keep_dice = tuple(die for die in dice if die in keep_values)

                    round_score += self.calculate_score(keep_dice)
                    num_dice -= len(keep_dice)

                    if num_dice != 0:
                        print(
                            f"You have {round_score} unbanked points and 0 dice remaining"
                        )

                        if round_score == 0:
                            print("No points scored in this round. Round ends.")
                        else:
                            total_score += round_score
                            print(
                                f"You banked {round_score} points in round {round_num}"
                            )
                            print(f"Total score is {total_score} points")

                        round_num += 1
                        break

                except ValueError:
                    print("Invalid input. Please try again.")


if __name__ == "__main__":
    gameR = GameLogic()
    gameR.play()
