"""

(c) Jippe Heijnen 2022
main.py created at 03/12/2022
Distributed under the Boost Software License v1.0.
(See license at https://www.boost.org/LICENSE_1_0.txt)

"""
from string import ascii_letters
from typing import List
from helpers import *


def findCommonItemType(input: str) -> int:
    result: int = 0
    front: str = input[int(len(input) / 2):]
    back: str = input[:int(len(input) / 2)]
    commonItemType: str = (lambda x: x)(*set(front) & set(back))
    result += ascii_letters.find(commonItemType) + 1
    return result


def findBatches(input: List[str]) -> List[int]:
    result: int = 0
    for i in range(2, len(input), 3):
        first: str = input[i - 2]
        second: str = input[i - 1]
        third: str = input[i]
        batchItemType: str = next(iter(set(first) & set(second) & set(third)))
        result += ascii_letters.find(batchItemType) + 1
    return result


if __name__ == '__main__':
    print(sum([findCommonItemType(i) for i in getInput('input.txt')]))
    print(findBatches(getInput('input.txt')))
