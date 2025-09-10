min_element = -1
stack = []
def push(value: int) -> None:
    global min_element
    if not stack:
        min_element = value
        stack.append(value)
    elif value >= min_element:
        stack.append(value)
    else:
        encoded_value = 2 * value - min_element
        stack.append(encoded_value)
        min_element = value

def pop() -> int:
    global min_element
    if not stack:
        return -1
    top_value = stack.pop()
    if top_value >= min_element:
        return top_value
    else:
        original_min = min_element
        min_element = 2 * min_element - top_value
        return original_min

def get_min():
    """

    :return:
    """
    if not stack:
        return -1
    return min_element


if __name__ == "__main__":
    push(3)
    print(get_min())  # Output: 3
    push(5)
    print(get_min())  # Output: 3
    push(2)
    print(get_min())  # Output: 2
    push(1)
    print(get_min())  # Output: 1
    pop()
    print(get_min())  # Output: 2
    pop()
    print(get_min())  # Output: 3
    pop()
    print(get_min())  # Output: 3