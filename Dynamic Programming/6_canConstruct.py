def canConstruct(word, arr):
    if word is None: return True

    for a in arr:
       if word.index(a) == 0:
           suffix = word[len(a):]
           if canConstruct(suffix, arr):
               return True
           
           
    return False



print(canConstruct('Anil', ['A', 'nil']))
print(canConstruct('Watermelon', ['water', 'n']))
           
           
           