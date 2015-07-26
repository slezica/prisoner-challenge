# Prisoner Challenge

A simulation of the [Prisonner's Dilemma](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma),
with several competing strategies playing against every other.

Each match has 300 rounds, each strategy is paired against each other once.

Strategies are located in [players.py](players.py).


# Running

    $ bin/run  # run the simulation
    $ bin/test # run tests with pytest


# Current Results:

Results vary among executions (some strategies include random factors),
but very little (< 1%) and rarely altering order.

    Strategy                  Score   Relative
    ------------------------------------------
    NiceTitForTat             9614    1.00
    VeryNiceTitForTat         9528    0.99
    ForgivingRetaliation      9425    0.98
    FairIsFair                9381    0.98
    TitForTat                 9280    0.97
    Pavlov                    9236    0.96
    LongTermTrust             9159    0.95
    MassiveRetaliation        9025    0.94
    Jesus                     8874    0.92
    SuspiciousTitForTat       8510    0.89
    Random                    8339    0.87
    OportunisticTitForTat     7621    0.79
    Satan                     7256    0.75


# Observations

- As soon as strategies got smarter, I could never beat `NiceTitForTat`
- Making `NiceTitForTat` `VeryNice` makes little difference, and for the worse
- `ForgivingRetaliation` seems arbitrary, is very close to `NiceTitForTat`
- `Satan` wins every individual duel, but is the worst overall
- `OportunisticTitForTat` is worse than random
- The difference between the best and worst strategies is 25%
- Playing less than 300 rounds (30) alters order, but NiceTitForTat still wins
- Playing more than 300 rounds (30000) makes no significant difference
