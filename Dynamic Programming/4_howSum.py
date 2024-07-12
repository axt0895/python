def bestSum(target, arr, memo = []):
    if target < 0: return -1
    if target == 0: return []
    
    for num in arr:
        remainder = target - num
        remainderResult = bestSum(remainder, arr, memo)
        if remainderResult != -1:
            memo.append(num)
            return memo
    return -1 


print(bestSum(100, [3, 9, 13])) 