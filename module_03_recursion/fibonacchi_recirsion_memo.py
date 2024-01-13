def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
        return n
    else:
        value = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
        memo[n] = value
        return value


print(fibonacci_memo(8))


# Кешування за допомогою Python декоратора

# from functools import lru_cache

# @lru_cache(maxsize=None)  # Unbounded cache
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(5))
