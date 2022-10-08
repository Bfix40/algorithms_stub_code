from collections.abc import Sequence
from timeit import default_timer
def decimal_to_binary(no_of_variable: int, minterms:Sequence[float]) -> list[str]:
    """
    >>> decimal_to_binary(3,[1.5])
    ['0.00.01.5']
    """
    temp = []
    for minterm in minterms:
        string = ""
        for i in range(no_of_variable):
            string = str(minterm % 2) + string
            minterm //= 2
        temp.append(string)
    return temp


start = default_timer()
decimal_to_binary(3, [1.5])
finish = default_timer()
print(finish - start)
