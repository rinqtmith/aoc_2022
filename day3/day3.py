import os
import sys
import string
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


def calculatePoints(arr: List[str]) -> int:
    total = 0
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    for x in arr:
        if x in lower:
            total += lower.index(x) + 1
        if x in upper:
            total += upper.index(x) + 27

    return total


# return type should be changed according to problem
def findSolution(arg: str) -> Tuple[int, int]:
    data = getInputs(arg)
    data1 = [x[: int(len(x) / 2)] for x in data if x != "\n"]
    data2 = [x[int(len(x) / 2) : len(x)] for x in data if x != "\n"]  # noqa

    result: List[str] = []

    for ind, val in enumerate(data1):
        temp = list(set(val) & set(data2[ind]))
        if temp:
            result.append(temp[0])

    return (calculatePoints(result), 1)


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
