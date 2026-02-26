"""
Problem 6: Merge Intervals

You are given an array of intervals, where each interval 
is represented as [start, end].

Write a function merge_intervals(intervals) that merges all 
overlapping intervals and returns a new array of the merged, 
non-overlapping intervals.

Example Usage:
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals)

intervals = [[1, 4], [4, 5]]
merge_intervals(intervals)

Example Output:
[[1, 6], [8, 10], [15, 18]]
[[1, 5]]
"""


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    return []


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    merge_intervals(intervals)

    intervals = [[1, 4], [4, 5]]
    merge_intervals(intervals)
