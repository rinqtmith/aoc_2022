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


# return type should be changed according to problem
def findSolution(arg: str) -> Tuple[int, int]:
    data = getInputs(arg)
    newData: List[List[str]] = [x.split(sep=",") for x in data]

    result = 0

    for pair in newData:
        first = set(
            range(int(pair[0].split(sep="-")[0]), int(pair[0].split(sep="-")[1]) + 1)
        )
        second = set(
            range(int(pair[1].split(sep="-")[0]), int(pair[1].split(sep="-")[1]) + 1)
        )
        inter = first & second
        if list(inter) == list(first) or list(inter) == list(second):
            result += 1

    return (result, 999)


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
