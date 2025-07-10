from collections import deque


def nearest_smaller_to_right(arr):
    """
    Given an array of integers, find the nearest smaller number to the right for each element.
    """

    stack_list = deque()
    result = [-1] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        while stack_list and stack_list[-1] >= arr[i]:
            stack_list.pop()
        if stack_list:
            result[i] = stack_list[-1]
        stack_list.append(arr[i])
    return result


# Example usage:
if __name__ == "__main__":
    arr = [4, 5, 2, 10, 8]
    print(nearest_smaller_to_right(arr))  # Output: [2, 2, -1, 8, -1]

    arr = [1, 3, 0, 2, 5]
    print(nearest_smaller_to_right(arr))  # Output: [0, 0, -1, -1, -1]
