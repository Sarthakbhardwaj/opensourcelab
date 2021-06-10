


letters = ['a','b','c','d','e','f','g','h','i','j','k','m','l','n','o','p','q','r','s','t' ,'u','v','w','x','y','z']
mutate = lambda x: [''.join([x[:i], l, x[i+1:len(x)]])
                    for i in range(len(x)) 
                    for l in letters]

words = mutate("hello")
#print(words)
x = "helll"
if x in words:
    print("true")
else:
    print("false")