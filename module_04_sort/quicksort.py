def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


print(quicksort([5, 3, 8, 4, 2]))
# Виведе: [2, 3, 4, 5, 8]

# Часова складність — O(n⋅log(n)) у середньому випадку, але O(n^2) у найгіршому випадку.