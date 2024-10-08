def bestSum(target, arr, memo = []):
    if target == 0: return []
    if target < 0: return -1
    
    shortestLength = None
    
    for num in arr:
        remainder = target - num
        remainderResult = bestSum(remainder, arr, memo)
        if remainderResult != -1:
            memo.append(num)
            if len(memo) < len(shortestLength):
                pass
            
        
    return -1





print(bestSum(7, [5, 3, 4, 7]))
print(bestSum(8, [5, 3, 2]))
print(bestSum(8, [1, 4, 5]))
print(bestSum(100, [1, 2, 5, 25]))