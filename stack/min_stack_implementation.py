# Min Element Using Stack

stack = []
extra_stack = []

# [11, 15, 13, 45, 60, 22]

def push(element):
    """
    """
    stack.append(element)
    if not extra_stack or (extra_stack and element < extra_stack[-1]):
        extra_stack.append(element)
    print("After Push")
    print(f"stack--->{stack}")
    print(f"extra_stack--->{extra_stack}")


def pop():
    """
    """
    if not stack:
        return -1

    popped_ele = stack.pop()
    if popped_ele <= extra_stack[-1]:
        extra_stack.pop()
    print("After Pop")
    print(f"stack--->{stack}")
    print(f"extra_stack--->{extra_stack}")


def get_min():
    """
    """
    print("Getting Minimum value:")
    if not extra_stack:
        return -1
    return extra_stack[-1]


def lets_play():
    """
    """
    while True:
        raw_input = int(input("Enter you option: "))
        if raw_input == 3:
            print("Exiting Loop")
            break;
        if raw_input == 0:
            element = int(input("Push Option Enter your Element: "))
            push(element)
        if raw_input == 1:
            pop()
        if raw_input == 2:
            value = get_min()
            print(f"Min Value {value}")


lets_play()