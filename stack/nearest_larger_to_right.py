from collections import deque


def nearest_larger_number_to_right(arr):
    """
    This function finds the nearest larger number to the right for each element in the array.
    """
    stack_list = deque([])
    result = [-1] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        while stack_list and stack_list[-1] <= arr[i]:
            stack_list.pop()
        if stack_list:
            result[i] = stack_list[-1]
        stack_list.append(arr[i]) # Add the current element to the stack
    return result

# Example usage:
if __name__ == "__main__":
    arr = [4, 5, 2, 10, 8]
    print(nearest_larger_number_to_right(arr))  # Output: [5, 10, 10, -1, -1]

    arr = [3, 2, 1]
    print(nearest_larger_number_to_right(arr))  # Output: [-1, -1, -1]

    arr = [1, 3, 2, 4]
    print(nearest_larger_number_to_right(arr))  # Output: [3, 4, 4, -1]