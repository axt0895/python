def fibonacci(num, memo = {}):
    if num in memo: return memo[num]
    if num <= 2: return 1
    else:
        memo[num] =fibonacci(num-1) + fibonacci(num - 2)
        return memo[num]


print(fibonacci(12))
print(fibonacci(7))
print(fibonacci(170))
print(fibonacci(400))