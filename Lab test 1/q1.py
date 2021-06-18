def isAlphabaticOrder(s):
    n = len(s)

    c = [s[i] for i in range(len(s))]

    c.sort(reverse=False)

    for i in range(n):
        if (c[i] != s[i]):
            return False

    return True
s = 'aabbababa'
print("For string: ")
print(s)
if (isAlphabaticOrder(s)):
    print("TRUE")
else:
    print("FALSE")

s = 'acefin'
print("for string:")
print(s)
if (isAlphabaticOrder(s)):
    print("TRUE")
else:
    print("FALSE")