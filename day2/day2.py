import os
import sys
from typing import List, Tuple

# Get inputs from files
input: str = os.path.dirname(__file__) + "/input"
input_ex: str = os.path.dirname(__file__) + "/input_ex"

# Use "py main.py test" for testing, use "py main.py" for solving
run_type: str = sys.argv[1] if len(sys.argv) > 1 else "no-args"


# Check argument
def checkArg(arg: str) -> bool:
    if arg not in ["test", "no-args"]:
        return False
    return True


# Get data lines from input
# Method and return type may change
def getInputs(arg: str) -> List[str]:
    with open(arg) as file:
        data = file.readlines()

    return [x[:-1] for x in data]


def playGame(first: str, second: str) -> int:
    if first == "A" and second == "X":
        return 4
    if first == "A" and second == "Y":
        return 8
    if first == "A" and second == "Z":
        return 3
    if first == "B" and second == "X":
        return 1
    if first == "B" and second == "Y":
        return 5
    if first == "B" and second == "Z":
        return 9
    if first == "C" and second == "X":
        return 7
    if first == "C" and second == "Y":
        return 2
    if first == "C" and second == "Z":
        return 6

    return 0


def playGame2(first: str, second: str) -> int:
    if first == "A" and second == "X":
        return 3
    if first == "A" and second == "Y":
        return 4
    if first == "A" and second == "Z":
        return 8
    if first == "B" and second == "X":
        return 1
    if first == "B" and second == "Y":
        return 5
    if first == "B" and second == "Z":
        return 9
    if first == "C" and second == "X":
        return 2
    if first == "C" and second == "Y":
        return 6
    if first == "C" and second == "Z":
        return 7

    return 0


# return type should be changed according to problem
def findSolution(arg: str) -> Tuple[int, int]:
    data = getInputs(arg)
    plays = [playGame(x.split(sep=" ")[0], x.split(sep=" ")[1]) for x in data]
    plays2 = [playGame2(x.split(sep=" ")[0], x.split(sep=" ")[1]) for x in data]

    return (sum(plays), sum(plays2))


def main() -> None:
    if not checkArg(run_type):
        print("Wrong argument!")
    else:
        if run_type == "test":
            print(findSolution(input_ex))
        else:
            print(findSolution(input))


if __name__ == "__main__":
    main()
