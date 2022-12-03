"""

(c) Jippe Heijnen 2022
helpers.py created at 03/12/2022
Distributed under the Boost Software License v1.0.
(See license at https://www.boost.org/LICENSE_1_0.txt)

"""

from typing import List

def getInput(input: str) -> List:
    file = List[str]
    file = []
    with open(input) as f:
        for line in f:
            file.append(line.strip('\n'))
    return file
