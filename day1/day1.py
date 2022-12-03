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
        data = file.read()

    return data.split(sep="\n\n")


# return type should be changed according to problem
def findSolution(arg: str) -> Tuple[int, int]:
    data = getInputs(arg)
    newData: List[List[int]] = [
        [int(y) for y in x.split(sep="\n") if y != ""] for x in data
    ]
    intData: List[int] = [sum(x) for x in newData]

    intData.sort(reverse=True)

    return max(intData), sum(intData[:3])


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
