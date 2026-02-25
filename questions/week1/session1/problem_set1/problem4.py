"""
Problem 4: Non-decreasing Array

Given an array nums with n integers, write a function non_decreasing() 
that checks if nums could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds 
for every i (0-based) such that (0 <= i <= n - 2).

Example Usage:
nums = [4, 2, 3]
non_decreasing(nums)

nums = [4, 2, 1]
non_decreasing(nums)

Example Output:
True
False
"""


def non_decreasing(nums: list[int]) -> bool:
    return True


if __name__ == "__main__":
    nums = [4, 2, 3]
    print(non_decreasing(nums))

    nums = [4, 2, 1]
    print(non_decreasing(nums))
