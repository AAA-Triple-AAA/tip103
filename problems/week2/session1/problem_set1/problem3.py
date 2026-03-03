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


def find_duplicate_chests(chests: list[int]) -> list[int]:
    return []


if __name__ == "__main__":
    chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
    chests2 = [1, 1, 2]
    chests3 = [1]

    print(find_duplicate_chests(chests1))
    print(find_duplicate_chests(chests2))
    print(find_duplicate_chests(chests3))
