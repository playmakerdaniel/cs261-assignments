# Name: Daniel D. Burrows
# OSU Email: burrdani@oregonstate.edu
# Course: CS261 - Data Structures (400)
# Assignment 1: Python Fundamentals Review
# Due Date: 4/18/2025
# Description: There are 10 separate problems in this assignment. For each problem, you will write a
# Python function according to the provided specifications. The skeleton code and some basic
# test cases for each problem are provided in the file assignment1.py
# Most problems will take as input (and sometimes return as output) an object of the
# StaticArray class. The StaticArray class has been pre-written for you, and is located in the
# file static_array.py


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------


def min_max(arr: StaticArray) -> tuple[int, int]:
    """ We want our function to return a tuple that contains the minimum and maximum in the StaticArray. """

    #If our array is empty, we raise an error. Useful for debugging.
    if arr.length()== 0:
        raise ValueError("Static Array is empty")

    #Initialize min_val and max_val with the first element of the array
    min_val = arr.get(0)
    max_val = arr.get(0)


    #Loop through the rest of the array starting at index i
    for i in range(1, arr.length()):
        value = arr.get(i)
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    return min_val, max_val

# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------


def fizz_buzz(arr: StaticArray) -> StaticArray:
    """ We will return a new Static Array where:
        multiples of 3 are replace with "fizz",
        multiples of 5 are placed with "buzz",
        and multiples of 3 and 5 (15) are replaced with "fizzbuzz".
    """
    # We will create a new array with the same length
    result = StaticArray(arr.length())

    # Now we loop through the original array
    for i in range(arr.length()):
        val = arr.get(i)

    # We will now check for divisibility of 15 first to avoid any overlap
        if val % 15 == 0:
            result.set(i, "fizzbuzz")
        elif val % 3 == 0:
            result.set(i, "fizz")
        elif val % 5 == 0:
            result.set(i, "buzz")
        else:
            result.set(i, val)

    return result

# ------------------- PROBLEM 3 - REVERSE -----------------------------------


def reverse(arr: StaticArray) -> None:
    """
    Reverses the elements of the StaticArray in-place.
    """
    left = 0
    right = arr.length() - 1

    while left < right:
        # Swap values at left and right
        temp = arr.get(left)
        arr.set(left, arr.get(right))
        arr.set(right, temp)

        left += 1
        right -= 1

# ------------------- PROBLEM 4 - ROTATE ------------------------------------


def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    Returns a new StaticArray with elements rotated by 'steps'.
    Positive steps rotate right, negative steps rotate left.
    """
    length = arr.length()
    result = StaticArray(length)

    # Normalize steps to be within array bounds
    steps = steps % length

    for i in range(length):
        # Compute new index after rotation
        new_index = (i + steps) % length
        result.set(new_index, arr.get(i))

    return result


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------


def sa_range(start: int, end: int) -> StaticArray:
    """
    Returns a StaticArray containing all integers from start to end inclusively.
    """
    # Calculate how many elements are needed
    size = abs(end - start) + 1

    # Create a new StaticArray of the required size
    result = StaticArray(size)

    # Determine direction of the range (increasing or decreasing)
    step = 1 if start <= end else -1

    # Populate the array with values from start to end
    for i in range(size):
        result.set(i, start + i * step)

    return result


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------


def is_sorted(arr: StaticArray) -> int:
    """
    Determines if a StaticArray is sorted.
    Returns:1 if sorted in ascending order, -1 if sorted in descending order, and 0 if not sorted
    """

    if arr.length() <= 1:
        return 1

    # Track whether the array remains strictly ascending or descending
    ascending = True
    descending = True

    # Compare each adjacent pair of values
    for i in range(1, arr.length()):
        prev = arr.get(i - 1)
        curr = arr.get(i)

        # If current value is less than or equal to previous, not strictly ascending
        if curr <= prev:
            ascending = False

        # If current value is greater than or equal to previous, not strictly descending
        if curr >= prev:
            descending = False

    # Return based on the final direction of the array
    if ascending:
        return 1

    if descending:
        return -1

    return 0

# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------


def find_mode(arr: StaticArray) -> tuple[object, int]:
    """
    Finds the mode (most frequent value) in a sorted StaticArray.
    Returns a tuple of the value and its frequency.
    """
    if arr.length() == 0:
        raise ValueError("Array is empty")

    mode_value = arr.get(0)
    mode_count = 1
    current_value = arr.get(0)
    current_count = 1

    for i in range(1, arr.length()):
        val = arr.get(i)

        # If same as previous, increment current count
        if val == current_value:
            current_count += 1
        else:
            # New value encountered; check if last one was the new mode
            if current_count > mode_count:
                mode_value = current_value
                mode_count = current_count

            # Reset tracking for new value
            current_value = val
            current_count = 1

    # Final check after loop ends
    if current_count > mode_count:
        mode_value = current_value
        mode_count = current_count

    return mode_value, mode_count


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------


def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    Returns a new StaticArray with all duplicates removed.
    Assumes the input array is sorted.
    """
    if arr.length() == 0:
        return StaticArray(0)

        # First pass: count how many unique elements are present
    unique_count = 1
    for i in range(1, arr.length()):
        if arr.get(i) != arr.get(i - 1):
            unique_count += 1

    # Create a new StaticArray of the correct size
    result = StaticArray(unique_count)

    # Set the first unique value
    result.set(0, arr.get(0))

    # Track the index for inserting into the new array
    index = 1

    # Second pass: copy unique elements to result array
    for i in range(1, arr.length()):
        if arr.get(i) != arr.get(i - 1):
            result.set(index, arr.get(i))
            index += 1

    return result


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    Sorts a StaticArray of integers using counting sort in descending order.
    Returns a new StaticArray with the sorted values.
    """
    if arr.length() == 0:
        return StaticArray(0)

    min_val = arr.get(0)
    max_val = arr.get(0)

    # Find the minimum and maximum value in the array
    for i in range(1, arr.length()):
        val = arr.get(i)
        if val < min_val:
            min_val = val
        elif val > max_val:
            max_val = val

    range_size = max_val - min_val + 1
    count_arr = StaticArray(range_size)

    # Initialize all counts to 0
    for i in range(range_size):
        count_arr.set(i, 0)

    # Count occurrences of each number
    for i in range(arr.length()):
        val = arr.get(i)
        index = val - min_val
        count_arr.set(index, count_arr.get(index) + 1)

    result = StaticArray(arr.length())
    result_index = 0

    # Fill the result array in descending order
    for i in range(range_size - 1, -1, -1):
        value = i + min_val
        count = count_arr.get(i)

        for _ in range(count):
            result.set(result_index, value)
            result_index += 1

    return result


# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------


def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    Returns a new StaticArray containing the squares of each value
    in sorted order. Assumes input array is sorted.
    """
    length = arr.length()
    result = StaticArray(length)

    left = 0
    right = length - 1
    index = length - 1

    # Traverse from both ends, placing the largest squares at the end
    while left <= right:
        left_val = arr.get(left)
        right_val = arr.get(right)

        if abs(right_val) >= abs(left_val):
            result.set(index, right_val * right_val)
            right -= 1
        else:
            result.set(index, left_val * left_val)
            left += 1

        index -= 1

    return result


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result is not None and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(f"Before: {arr}")
        result = count_sort(arr)
        print(f"After : {result}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-10 ** 9, 10 ** 9 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
