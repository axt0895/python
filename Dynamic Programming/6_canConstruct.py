def can_construct(target, arr, memo = {}):
    if target in memo: return  memo[target]
    if target == '': return True
    for word in arr:
        if target.startswith(word):
            new_target = target[len(word):]
            if can_construct(new_target, arr, memo):
                memo[target] = True
                return True

    memo[target] = False
    return False



print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'adcd']))
print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eeee', 'eeeeee', 'eeeeeee', 'eeeeeeee']))
