"""
Problem 5: Three Sum
Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, 
and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example Usage:
nums = [-1, 0, 1, 2, -1, -4]
three_sum(nums)

nums = [0, 1, 1]
three_sum(nums)

nums = [0, 0, 0]
three_sum(nums)

Example Output:
[[-1, -1, 2], [-1, 0, 1]]
[]
[[0, 0, 0]]
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    pairs = {}

    for i, num in enumerate(nums):
        diff = abs(target - num)
        if diff in pairs:
            return [diff, num]
        pairs[num] = i

    return []


def three_sum(nums: list[int]) -> list[list[int]]:
    res: list[list[int]] = []

    for num in nums:
        t_sum = two_sum(nums, 0 - num)
        if t_sum:
            res.append([num, t_sum[0], t_sum[1]])

    return res


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(three_sum(nums))

    nums = [0, 1, 1]
    print(three_sum(nums))

    nums = [0, 0, 0]
    print(three_sum(nums))
