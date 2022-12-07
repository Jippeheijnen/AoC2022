"""

(c) Jippe Heijnen 2022
day7.py created at 07/12/2022
Distributed under the Boost Software License v1.0.
(See license at https://www.boost.org/LICENSE_1_0.txt)

"""

from enum import Enum
from typing import List


class type(Enum):
    """
    A little class to distinguish types from eachother
    """

    # folder stuff
    file = 0
    dir = 1
    # command stuff
    cd = 2
    ls = 3

class Command:
    def __init__(self, type: type):
        self.type: type = type

class CD_Command(Command):
    def __init__(self, dir_to_go_to: str):
        super().__init__(type.cd)
        self.dir_to_go_to: str = dir_to_go_to
        
    def __repr__(self):
        return f'$ cd {self.dir_to_go_to}'

class LS_Command(Command):
    def __init__(self, returns: List[str]):
        super().__init__(type.ls)
        self.returns: List[str] = returns
    
    def __repr__(self):
        return f'$ ls'
    
class FS_Item():
    def __init__(self, type: type, name: str, size: int = 0):
        self.type = type
        self.name:str = name
        self.size = size
        
    def __repr__(self):
        return f'{self.size} {self.name}'

class Tree_node:
    def __init__(self,
                 type: type,
                 name: str,
                 size: int = 0,
                 parent: 'Tree_node' = None):
        self.__type: type = type
        self.__size: int = size
        self.__name: str = name
        self.__parent: Tree_node = parent
        self.__items: List[FS_Item] = []
        self.__children: List[Tree_node] = []

    def __repr__(self) -> str:
        return f"{self.__name} {self.__items}"

    def addChild(self, child: 'Tree_node'):
        self.__children.append(child)
        
    def addItem(self, item: FS_Item):
        self.__items.append(item)

    def getChildren(self) -> List['Tree_node']:
        return self.__children

    def getSize(self):
        return self.__size
