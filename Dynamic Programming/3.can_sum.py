def canSum(target, arr, memo = {}):
    if target in memo: return memo[target]
    if target < 0: return False
    if target == 0: return True
    
    for num in arr:
        remainder = target - num
        if canSum(remainder, arr):
            memo[target] = True
            return True
        
    memo[target] = False
    return False



print(canSum(500, [1, 2, 3, 4, 5]))