from collections import deque


def nearest_larger_number_to_left(arr):
    """
    This function finds the nearest larger number to the left for each element in the array.
    """
    stack_list = deque([])
    result = [-1] * len(arr)
    for i in range(len(arr)):
        while stack_list and stack_list[-1] <= arr[i]:
            stack_list.pop()
        if stack_list:
            result[i] = stack_list[-1]
        stack_list.append(arr[i])  # Add the current element to the stack
    return result

# Example usage:
if __name__ == "__main__":
    arr = [4, 5, 2, 10, 8]
    print(nearest_larger_number_to_left(arr))  # Output: [-1, -1, 5, -1, 10]

    arr = [3, 2, 1]
    print(nearest_larger_number_to_left(arr))  # Output: [-1, 3, 2]

    arr = [1, 3, 2, 4]
    print(nearest_larger_number_to_left(arr))  # Output: [-1, -1, 3, -1]
