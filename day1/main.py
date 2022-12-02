from typing import List, Union


def getElfCalorieSums(input : str) -> List[int]:
    file = List[Union[int, str]]
    file = []
    caloriesPerElf = List[int]
    caloriesPerElf = []
    elfCaloriesSums = List[int]
    elfCaloriesSums = []
    with open(input) as f:
        for line in f:
            try:
                file.append(int(line.strip('\n')))
            except ValueError:
                file.append("")

    for i in range(len(file)):
        if file[i] != "":
            caloriesPerElf.append(file[i])
        else:
            elfCaloriesSums.append(sum(caloriesPerElf))
            caloriesPerElf = []
    return elfCaloriesSums

def getTopThreeElfCalories(input : List[int]) -> List[int]:
    topThree = List[int]
    topThree = []
    for i in range(3):
        topThree.append(max(input))
        input.remove(max(input))
    return topThree


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(max(getElfCalorieSums('input.txt')))
    print(sum(getTopThreeElfCalories(getElfCalorieSums('input.txt'))))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
