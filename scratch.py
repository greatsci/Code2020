def solve(s):
    lst = s.split(' ')
    res = []
    for word in lst:
        if word[0].isalpha():
            res.append(word.capitalize())
        else:
            res.append(word)
    return ' '.join(res)

# Test
s = '12dsg'
print(s.split(' '))
print(s.capitalize())