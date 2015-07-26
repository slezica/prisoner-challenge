from src.engine import *
from src.players import Jesus, Satan


def match_avg(classes):
    players = play(classes, rounds = 10)
    return [ player.score / 10 for player in players ]


def test_play_round():
    jesus = Jesus()
    satan = Satan()

    assert play_round([ jesus, jesus ]) == [BOTH_COOPERATED] * 2
    assert play_round([ jesus, satan ]) == [HE_BETRAYED_ME, I_BETRAYED_HIM]
    assert play_round([ satan, jesus ]) == [I_BETRAYED_HIM, HE_BETRAYED_ME]
    assert play_round([ satan, satan ]) == [BOTH_BETRAYED] * 2


def test_play():
    assert match_avg([ Jesus, Jesus ]) == [BOTH_COOPERATED] * 2
    assert match_avg([ Jesus, Satan ]) == [HE_BETRAYED_ME, I_BETRAYED_HIM]
    assert match_avg([ Satan, Jesus ]) == [I_BETRAYED_HIM, HE_BETRAYED_ME]
    assert match_avg([ Satan, Satan ]) == [BOTH_BETRAYED] * 2
