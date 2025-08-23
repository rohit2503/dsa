def max_area_of_histogram(arr):
    """
    Calculate the maximum area of a histogram represented by an array of heights.
    :param arr:
    :return:
    """

    #  Approach 1
    stack = []
    max_area = 0
    index = 0

    while index < len(arr):
        # If this bar is higher than the bar at stack top, push it to the stack
        if not stack or arr[index] >= arr[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            # Pop the top
            top_of_stack = stack.pop()
            # Calculate the area with arr[top_of_stack] as the smallest (or minimum height) bar 'h'
            area = (arr[top_of_stack] *
                    ((index - stack[-1] - 1) if stack else index))
            # Update max area, if needed
            max_area = max(max_area, area)

    # Now pop the remaining bars from stack and calculate area with each popped bar
    while stack:
        top_of_stack = stack.pop()
        area = (arr[top_of_stack] *
                ((index - stack[-1] - 1) if stack else index))
        max_area = max(max_area, area)

    return max_area


def nearest_small_right(arr):
    """
    """

    # NSR
    # [4, 2, 1, 3, 4, 3, 2]
    # ans = [2, 1, -1, 2, 3, 2, -1]
    # index = [1, 2, 7, 6, 5, 6, 7]
    r_result = []
    r_stack = []

    for index in range(len(arr) - 1, -1, -1):

        while r_stack and arr[index] <= arr[r_stack[-1]]:
            r_stack.pop()

        if r_stack:
            r_result.append(r_stack[-1])
        else:
            r_result.append(len(arr))
        r_stack.append(index)

    r_result.reverse()
    return r_result


def nearest_small_left(arr):
    """
    """

    # NSR
    # [4, 2, 1, 3, 4, 3, 2]
    # ans = [-1, -1, -1, 1, 3, 1, 1]
    # index = [-1, -1, -1, 2, 3, 2, 2]
    r_result = []
    r_stack = []

    for index in range(len(arr)):

        while r_stack and arr[index] <= arr[r_stack[-1]]:
            r_stack.pop()

        if r_stack:
            r_result.append(r_stack[-1])
        else:
            r_result.append(-1)
        r_stack.append(index)
    return r_result


def calculate_area(arr):
    """
    """
    # Approach 2
    n_s_l = nearest_small_left(arr)
    n_s_r = nearest_small_right(arr)
    area = []
    for index in range(len(arr)):
        area.append((n_s_r[index] - n_s_l[index] - 1) * arr[index])

    return max(area)


hist = [4, 2, 1, 3, 4, 3, 2]

if __name__ == "__main__":
    # Example usage
    histogram = [2, 1, 5, 6, 2, 3]
    print("Maximum area in max_area_of_histogram histogram:", max_area_of_histogram(histogram))  # Output: 10
    print("Maximum area in calculate_area histogram:", calculate_area(histogram))  # Output: 10
    histogram = [6, 2, 5, 4, 5, 1, 6]
    print("Maximum area in max_area_of_histogram histogram:", max_area_of_histogram(histogram))  # Output: 12
    print("Maximum area in calculate_area histogram:", calculate_area(histogram))  # Output: 12
    histogram = [1, 2, 3, 4, 5]
    print("Maximum area in max_area_of_histogram histogram:", max_area_of_histogram(histogram))  # Output: 9
    print("Maximum area in calculate_area histogram:", calculate_area(histogram))  # Output: 9
    histogram = [4, 2, 1, 3, 4, 3, 2]
    print("Maximum area in max_area_of_histogram histogram:", max_area_of_histogram(histogram))  # Output: 9
    print("Maximum area in calculate_area histogram:", calculate_area(histogram))  # Output: 9