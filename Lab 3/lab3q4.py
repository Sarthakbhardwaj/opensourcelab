# def fun(variable):
#     letters = ['a', 'e', 'i', 'o', 'u']
#     if (variable in letters):
#         return True
#     else:
#         return False
  
  
# sequence = ['a', 'e', 'e', 'j', 'k', 's', 'p', 'r','i']
  
# filtered = filter(fun, sequence)
  
# print('The filtered letters are:')
# for s in filtered:
#     print(s)

names = ['ram', 'shyam', 'sam', 'aman', 'utkarsh']

def func(x):
  return x[0].lower() in 'aeiou'

new_names = filter(func, names)

print(list(new_names))