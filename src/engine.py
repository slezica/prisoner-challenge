from abc import ABCMeta, abstractmethod


HE_BETRAYED_ME  = 0
BOTH_BETRAYED   = 1
BOTH_COOPERATED = 3
I_BETRAYED_HIM  = 5


class Player(metaclass = ABCMeta):
    def __init__(self):
        self.score      = 0
        self.last_score = None
        self.generator  = self.play()

    def award(self, points):
        self.score += points
        self.last_score = points

    def decide(self):
        return next(self.generator)

    def he_cooperated(self):
        return self.last_score in [BOTH_COOPERATED, I_BETRAYED_HIM]

    def i_cooperated(self):
        return self.last_score in [BOTH_COOPERATED, HE_BETRAYED_ME]

    @abstractmethod
    def play(self):
        pass

    def __repr__(self):
        return "<{} {} points>".format(self.__class__.__name__, self.score)


def play_round(players):
    cooperates = [ player.decide() for player in players ]

    if all(cooperates):
        scores = [ BOTH_COOPERATED for player in players ]

    elif not any(cooperates):
        scores = [ BOTH_BETRAYED for player in players ]

    else:
        scores = [
            I_BETRAYED_HIM if not cooperates else HE_BETRAYED_ME
            for player, cooperates in zip(players, cooperates)
        ]

    for player, points in zip(players, scores):
        player.award(points)

    return scores


def play(PlayerClasses, rounds = 3):
    players = [ Player() for Player in PlayerClasses ]

    for round in range(rounds):
        play_round(players)

    return players
