def linear_search(arr, x):
    """
    Perform a linear search on the given list to find the index of the target element.
    Parameters:
    - arr (list): The list to search through.
    - x (any): The target element to find.
    Returns:
    - int: The index of the target element if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


def exists_in_list(arr, x):
    return linear_search(arr, x) != -1


numbers = [1, 3, 5, 7, 9, 11]
print(linear_search(numbers, 7))  # Output: 3
print(exists_in_list(numbers, 2))  # Output: False

# З точки зору часу виконання - у найгірщому випадку O(n), у середньому випадку - O(n/2)
