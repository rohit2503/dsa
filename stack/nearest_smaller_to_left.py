from collections import deque


def nearest_smaller_to_left(numbers):
    """
    Given an array of integers, find the nearest smaller number to the left for each element.
    """
    stack_list = deque()
    result = [-1] * len(numbers)

    for i in range(len(numbers)):
        while stack_list and stack_list[-1] >= numbers[i]:
            stack_list.pop()
        if stack_list:
            result[i] = stack_list[-1]
        stack_list.append(numbers[i])

    return result

# Example usage:
if __name__ == "__main__":
    arr = [4, 5, 2, 10, 8]
    print(nearest_smaller_to_left(arr))  # Output: [-1, 4, -1, 2, 2]

    arr = [1, 3, 0, 2, 5]
    print(nearest_smaller_to_left(arr))  # Output: [-1, 1, -1, 0, 2]