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


def is_even(num: int) -> bool:
    return num % 2 == 0


def is_odd(num: int) -> bool:
    return num % 2 != 0


def sort_by_parity(nums: list[int]) -> list[int]:
    i, j = 0, len(nums)-1

    while i < j:
        l_num = nums[i]
        r_num = nums[j]

        if is_even(l_num) and is_even(r_num):
            i += 1
        elif is_odd(l_num) and is_odd(r_num):
            j -= 1
        elif is_odd(l_num) and is_even(r_num):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        else:
            i += 1
            j -= 1

    return nums


if __name__ == "__main__":
    nums = [3, 1, 2, 4]
    print(sort_by_parity(nums))

    nums = [0]
    print(sort_by_parity(nums))
