def lengthOfLongestSubstring(s):
    a = 0
    b = 0
    l = {}
    result = 0
    while b < len(s):
        if s[b] not in l or a>l[s[b]]:
            result = max(result,(b-a+1))
            l[s[b]] = b
        else:
            a = l[s[b]]+1
            result = max(result,(b-a+1))
            b-=1
        b+=1
    return result

print(lengthOfLongestSubstring(''))