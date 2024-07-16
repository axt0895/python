def count_construct(target, arr, memo = {}):
    if target in memo: return memo[target]
    if target == '': return 1
    total_count = 0
    for word in arr:
        if target.startswith(word):
            new_target = target[len(word): ]
            count = count_construct(new_target, arr, memo)
            total_count += count

    memo[target] = total_count
    return total_count



print(count_construct('target', ['t', 'ar', 'ge', 'tar', 'get','targ', 'et', 'arg', 'et']))

print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(count_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eeee', 'eeeeee', 'eeeeeee', 'eeeeeeee']))
