"""
Problem 4: Sort Array by Parity

Given an integer array nums, write a function sort_by_parity() 
that moves all the even integers to the beginning of the array, 
followed by all the odd integers.

Return any array that satisfies this condition.

Example Usage:
nums = [3, 1, 2, 4]
sort_by_parity(nums)

nums = [0]
sort_by_parity(nums)

Example Output:
[2, 4, 3, 1]
[0]
"""


def sort_by_parity(nums: list[int]) -> list[int]:
    return []


if __name__ == "__main__":
    nums = [3, 1, 2, 4]
    print(sort_by_parity(nums))

    nums = [0]
    print(sort_by_parity(nums))
