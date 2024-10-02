def gridTraveler(m, n, memo= {}):
    key = str(m)+':'+str(n)
    if key in memo: return memo[key]
    if m == 1 and n == 1:
        return 1 
    elif m == 0 or n == 0:
        return 0
    else:
        memo[key] = gridTraveler(m-1,n, memo) + gridTraveler(m, n-1, memo)
        return memo[key]
    
    
    
print(gridTraveler(9, 10))
print(gridTraveler(9, 4))
print(gridTraveler(4, 7))
print(gridTraveler(2, 2))
print(gridTraveler(50, 50))