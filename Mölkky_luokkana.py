"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Code template for Mölkky.
"""


class Player:
    """

    """
    def __init__(self, player):
        self.__player = player
        self.__points = 0
        self.__throws = 0
        self.__count_hits = 0
        self.__thrown_points = 0

    def get_name(self):
        return self.__player

    def get_points(self):
        return self.__points

    def get_thrown_points(self):
        return self.__thrown_points

    def add_points(self, points):
        self.__thrown_points += points

        if self.__points + points > 50:
            print(f"{self.__player} gets penalty points!")
            self.__points = 25

        else:
            self.__points += points

        if 40 <= self.__points <= 49:
            print(f"{self.__player} needs only {50 - self.__points} points. "
                  f"It's better to avoid knocking down the pins with higher"
                  f" points.")
        self.__throws += 1
        if points > 0:
            self.__count_hits += 1

    def has_won(self):
        if self.__points == 50:
            return True
        else:
            return False

    def average_points(self):
        average = self.__thrown_points / self.__throws
        return average

    def count_hit_percentage(self):
        try:
            percentage = self.__count_hits / self.__throws * 100
        except ZeroDivisionError:
            return 0.0
        return percentage


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        if in_turn.average_points() < pts:
            print(f"Cheers {in_turn.get_name()}!")

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(f"{player1.get_name()}: {player1.get_points()} p, hit percentage"
              f" {player1.count_hit_percentage():.1f}")
        print(f"{player2.get_name()}: {player2.get_points()} p, hit percentage"
              f" {player2.count_hit_percentage():.1f}")
        print("")

        throw += 1


if __name__ == "__main__":
    main()
