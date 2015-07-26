import random
from .engine import Player


def chance(prob_of_true):
    return random.random() < prob_of_true


class Jesus(Player):
    "Always cooperates"

    def play(self):
        while 1: yield True


class Satan(Player):
    "Always betrays"

    def play(self):
        while 1: yield False


class Random(Player):
    "Behaves randomly"

    def play(self):
        while 1: yield chance(.5)


class TitForTat(Player):
    "Cooperates first, then does what opponent did"

    def play(self):
        yield True

        while 1:
            yield self.he_cooperated()


class NiceTitForTat(Player):
    "Cooperates first, then does what opponent did, but forgives 10%"

    def play(self):
        yield True

        while 1:
            if self.he_cooperated():
                yield True
            else:
                yield chance(.1)


class VeryNiceTitForTat(Player):
    "Cooperates first, then does what opponent did, but forgives 50%"

    def play(self):
        yield True

        while 1:
            if self.he_cooperated():
                yield True
            else:
                yield chance(.5)



class SuspiciousTitForTat(Player):
    "Betrays first, then does what opponent did"

    def play(self):
        yield False

        while 1:
            yield self.he_cooperated()


class OportunisticTitForTat(Player):
    "Cooperates first, then does what opponent did, but betrays extra 10%"

    def play(self):
        yield True

        while 1:
            if self.he_cooperated():
                yield chance(.9)
            else:
                yield False


class MassiveRetaliation(Player):
    "Cooperates until betrayed, then betrays forever"

    def play(self):
        while 1:
            yield True
            if not self.he_cooperated(): break

        while 1:
            yield False


class ForgivingRetaliation(Player):
    "Cooperates until betrayed, then BBBB-CC"

    def play(self):
        yield True

        while 1:
            if not self.he_cooperated():
                for round in range(4): yield False
                for round in range(2): yield True

            yield True

class FairIsFair(Player):
    "Cooperates if rewarded for cooperation or punished for betrayal"

    def play(self):
        yield True
        yield False

        he_was_fair  = self.he_cooperated()
        my_last_move = False

        while 1:
            my_next_move = he_was_fair
            yield my_next_move

            he_was_fair  = (my_last_move == self.he_cooperated())
            my_last_move = my_next_move


class LongTermTrust(Player):
    "Cooperates if opponent tends to cooperate >50%"

    def play(self):
        n_rounds = 0
        n_coops  = 0
        yield True

        while 1:
            n_rounds += 1
            n_coops  += int(self.he_cooperated())

            yield n_coops > 0 and (n_rounds / n_coops > 0.5)


class Pavlov(Player):
    "Repeats choice if rewarded"

    def play(self):
        yield True

        while 1:
            yield self.he_cooperated()
