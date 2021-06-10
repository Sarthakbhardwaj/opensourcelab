# def myfunc(a, b):
#   return a + b

# x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

# print(x)
# print(list(x))

def square(n):
    return n*n
a = (1, 2, 3, 4)
result = map(square, a)
print(result)
for i in result:
    print(i)