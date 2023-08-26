def merge_the_tools(s, k):
    for i in range(0, len(s), k):
        sub = s[i:i+k]
        new_sub = ""
        for char in sub:
            if char not in new_sub:
                new_sub += char
        print(new_sub)

s = 'AABCAAADA'
k = 3
merge_the_tools(s, k)
