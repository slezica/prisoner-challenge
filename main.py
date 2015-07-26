from pprint import pprint
from itertools import combinations

from src.engine import Player, play
from src.players import *

N_ROUNDS = 300

classes = Player.__subclasses__()
# classes = [Satan, TitForTat]

matches = list(combinations(classes, 2))
scores  = { PlayerClass: 0 for PlayerClass in classes }


for match in matches:
    for player in play(match, rounds = N_ROUNDS):
        scores[player.__class__] += player.score


best_score = max(scores.values())

for cls in sorted(scores, key = scores.get, reverse = True):
    name   = cls.__name__
    score  = scores[cls]
    rscore = score / best_score

    print("{:<25} {:<7} {:.2f}".format(name, score, rscore))
