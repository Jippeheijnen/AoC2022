"""

(c) Jippe Heijnen 2022
main.py created at 04/12/2022
Distributed under the Boost Software License v1.0.
(See license at https://www.boost.org/LICENSE_1_0.txt)

"""

from typing import List
from helpers import *

def allInefficientPairsN(input: List[str]) -> int:
    elf1: List[int] = []
    elf2: List[int] = []
    inefficientPairsN: int = 0
    for pair in input:
        elf1, elf2 = [[int(j) for j in i.split('-')] for i in pair.split(',')]
        if (elf1[0] <= elf2[0] <= elf1[1] and elf1[0] <= elf2[1] <= elf1[1]) or \
                (elf2[0] <= elf1[0] <= elf2[1] and elf2[0] <= elf1[1] <= elf2[1]):
            inefficientPairsN += 1
    return inefficientPairsN

def allOverlappingPairsN(input: List[str]) -> int:
    elf1: List[int] = []
    elf2: List[int] = []
    overlappingPairsN: int = 0
    for pair in input:
        elf1, elf2 = [[int(j) for j in i.split('-')] for i in pair.split(',')]
        if (elf1[0] <= elf2[0] <= elf1[1] or elf1[0] <= elf2[1] <= elf1[1]) or \
                (elf2[0] <= elf1[0] <= elf2[1] or elf2[0] <= elf1[1] <= elf2[1]):
            overlappingPairsN += 1
    return overlappingPairsN

if __name__ == '__main__':
    print(allInefficientPairsN(getInput('input.txt')))
    print(allOverlappingPairsN(getInput('input.txt')))