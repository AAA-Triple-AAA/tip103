"""
Problem 5: Container with Most Honey

Christopher Robin is helping Pooh construct the 
biggest hunny jar possible.

Help him write a function that accepts an integer array 
heights of length n. The height of each element is given 
by heights[i].

There are n vertical lines drawn such that the two endpoints 
of the ith line are (i, 0) and (i, heights[i]).

Find two lines that, together with the x-axis, form the 
container that holds the most honey.

Return the maximum amount of honey a container can store.

Notice that you may not slant the container.

Example Usage:
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
most_honey(height)

height = [1, 1]
most_honey(height)

Example Output:
49
1
"""


def most_honey(heights: list[int]) -> int:
    i = 0
    j = len(heights)-1

    max_area = 0

    while i < j:
        area = (j - i) * min(heights[i],  heights[j])
        max_area = max(max_area, area)
        if heights[i] < heights[j]:
            i += 1
        else:
            j -= 1

    return max_area


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(most_honey(height))

    height = [1, 1]
    print(most_honey(height))
