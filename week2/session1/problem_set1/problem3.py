"""
Problem 3: Find All Duplicate Treasure Chests in an Array

Captain Blackbeard has an integer array chests of length n where all 
the integers in chests are in the range [1, n] and each integer appears 
once or twice. Return an array of all the integers that appear twice, 
representing the treasure chests that have duplicates.

Example Usage:
chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))

Example Output:
[2, 3]
[1]
[]
"""
from collections import defaultdict


def find_duplicate_chests(chests: list[int]) -> list[int]:
    # res: list[int] = []

    # d = defaultdict(int)

    # for chest in chests:
    #     d[chest] += 1

    # for key in d.keys():
    #     if d[key] == 2:
    #         res.append(key)

    # return res

    seen = set()
    res = []

    for chest in chests:
        if chest in seen:
            res.append(chest)
        seen.add(chest)

    return res


if __name__ == "__main__":
    chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
    chests2 = [1, 1, 2]
    chests3 = [1]

    print(find_duplicate_chests(chests1))
    print(find_duplicate_chests(chests2))
    print(find_duplicate_chests(chests3))
