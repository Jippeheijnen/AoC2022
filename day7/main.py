"""

(c) Jippe Heijnen 2022
main.py created at 07/12/2022
Distributed under the Boost Software License v1.0.
(See license at https://www.boost.org/LICENSE_1_0.txt)

"""
from helpers import *
from day7 import *
from typing import List, Union


def folder_exists_in_fs(root_node: Tree_node, folder_dir: str) -> bool:
    path: List[str] = folder_dir.split('/')
    folder_exists: bool = False

    # todo: implement this

    # if len(root_node.getChildren()) != 0:

    return folder_exists


def processInput(input: List[str]) -> List[Command]:
    commands: List[Command] = []
    command_list_to_add: List[str] = []
    cur_dir: str = ''
    # need offset to remember the correct loop iterations
    i: int = 0
    command_list_to_add.append(input[i])
    try:
        while not input[i+1][0] == '$':
            i+=1
            command_list_to_add.append(input[i])
            continue
        return processInput(input[i+1:]) + [createCommand(command_list_to_add)]
    except IndexError:
        return [createCommand(command_list_to_add)]



def createCommand(command: List[str]) -> Union[CD_Command, LS_Command]:
    # dc = don't care because it's '$'.
    #  check for parameterless command
    if len(command[0].split()) == 2:
        dc, comm = command[0].split()
    else:
        dc, comm, path = command[0].split()
    if comm == 'cd':
        return CD_Command(path)
    elif comm == 'ls':
        # check if ls returned any items
        if not len(command) > 1:
            return LS_Command(list(None))
        else:
            return LS_Command(command[1:])


def createNodes(commands: List[Union[CD_Command, LS_Command]], root_node: Tree_node = Tree_node(type.dir, 'root'), working_dir: List[str] = []) -> Tree_node:
    if commands[0].type == type.cd:
        if not commands[0].dir_to_go_to == '..':
            new_node: Tree_node = Tree_node(type.dir, commands[0].dir_to_go_to, parent=root_node)
            working_dir.append(commands[0].dir_to_go_to)
            root_node.addChild(new_node)
        else:
            new_node: Tree_node = root_node
            working_dir.pop()
            root_node.addChild(new_node)
            return createNodes(commands[1:], root_node, working_dir)
    elif commands[0].type == type.ls:
            values: List[str] = commands[0].returns
            for i in range(len(values)):
                item: List[str] = values[i].split()
                name: str
                size: int
                # starts with number so we're adding a file here
                if values[i][0].isdigit():
                    size, name = item
                    root_node.addItem(FS_Item(type.file, name, size))
                # Directories added here
                else:
                    dc, name = item
                    root_node.addItem(FS_Item(type.dir, name))
            new_node = root_node
    # shave first command off the list
    return createNodes(commands[1:], new_node, working_dir)
    
            


if __name__ == '__main__':
    command_list: List[Union[CD_Command, LS_Command]] = processInput(getInput('input.txt'))
    command_list.reverse()
    root: Tree_node = \
        createNodes(command_list)
    print(f' size of root: {root.getSize()}')
