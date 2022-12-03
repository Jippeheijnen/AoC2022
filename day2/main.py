"""

(c) Jippe Heijnen 2022
main.py created at 02/12/2022
Distributed under the Boost Software License v1.0.
(See license at https://www.boost.org/LICENSE_1_0.txt)

"""
from typing import List

def calcGame(input: str) -> str:
    switch={
        'A':1, 1:'A', # rock
        'B':2, 2:'B', # paper
        'C':3, 3:'C', # scissors
        'X':1, # lose
        'Y':2, # draw
        'Z':3  # win
    }
    opponent: str = input[0]
    gameResult: str = input[2]
    us: str = ''
    if switch.get(gameResult) == 3:
        if opponent != 'C':
            us = switch.get(switch.get(opponent)+1)
        else:
            us = switch.get(switch.get(opponent)-2)

    elif switch.get(gameResult) == 2:
        us = opponent

    elif switch.get(gameResult) == 1:
        if opponent != 'A':
            us = switch.get(switch.get(opponent)-1)
        else:
            us = switch.get(switch.get(opponent)+2)

    return f"{opponent} {us}"



def calcScore(input: str) -> int:
    switch={
        'A':1, # rock
        'B':2, # paper
        'C':3 # scissors
    }
    opponent: int = switch.get(calcGame(input)[0])
    us: int = switch.get(calcGame(input)[2])

    score: int = 0

    # determining game states
    if opponent == us:
        score = 3 + us
    elif opponent + 1 == us:
        score = 6 + us
    elif opponent - 1 == us:
        score = 0 + us
    elif opponent + 2 == us:
        score = 0 + us
    elif opponent - 2 == us:
        score = 6 + us

    return score

def calcTotalScore(input: List[str]) -> int:
    totalScore: int = 0
    for i in range(len(input)):
        totalScore += calcScore(input[i])
    return totalScore

if __name__ == '__main__':
    print(calcTotalScore(getInput('input.txt')))
