"""

(c) Jippe Heijnen 2022
main.py created at 05/12/2022
Distributed under the Boost Software License v1.0.
(See license at https://www.boost.org/LICENSE_1_0.txt)

"""
from typing import List, Dict
from helpers import getInput

def crateMover9000(stacks: Dict[int, List[str]], 
                   instructions: List[List[int]]) \
        -> Dict[int, List[str]]:
    for instruction in instructions:
        nMoves:int = 0
        originStack:int = 0
        targetStack:int = 0
        nMoves, originStack, targetStack = instruction
        for i in range(nMoves):
            if not len(stacks[originStack]) == 0:
                movedBox: str = stacks[originStack].pop()
                stacks[targetStack].append(movedBox)
    return stacks

def crateMover9001(stacks: Dict[int, List[str]],
                   instructions: List[List[int]]) \
        -> Dict[int, List[str]]:
    for instruction in instructions:
        boxesToMove: List[str] = []
        nMoves:int = 0
        originStack:int = 0
        targetStack:int = 0
        nMoves, originStack, targetStack = instruction
        for i in range(nMoves):
            if not len(stacks[originStack]) == 0:
                boxesToMove.append(stacks[originStack].pop())
        boxesToMove.reverse()
        for box in boxesToMove:
            stacks[targetStack].append(box)
    return stacks

def showStackTops() -> str:
    stacks: Dict[int, List[str]] = {
        1: ['R','G','J','B','T','V','Z'],
        2: ['J','R','V','L'],
        3: ['S','Q','F'],
        4: ['Z','H','N','L','F','V','Q','G'],
        5: ['R','Q','T','J','C','S','M','W'],
        6: ['S','W','T','C','H','F'],
        7: ['D','Z','C','V','F','N','J'],
        8: ['L','G','Z','D','W','R','F','Q'],
        9: ['J','B','W','V','P'] }
    
    instructions: List[List[int]] = [i.split() for i in getInput('input.txt')[10:]]
    instructions = [[int(j) for j in i if j not in 'movefromto'] for i in instructions]
    stacks = crateMover9001(stacks, instructions)
    result: str = ''
    for i in stacks.values():
            if len(i) != 0:
                result += i[-1]
    
    return result

if __name__ == '__main__':
    print(showStackTops())