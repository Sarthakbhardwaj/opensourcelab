import numpy as np
import matplotlib.pyplot as plt

# def q1():
#     pi = np.pi
#     vals = np.array([-pi, -pi/4, -pi/2, 0, pi/4, pi/2, pi])
#     x = np.array(["-pi", "-pi/4", "-pi/2", "0", "pi/4", "pi/2", "pi"])
#     tan, cot, sec, cosec = np.tan(vals), 1/np.tan(vals), 1/np.cos(vals), 1/np.sin(vals)
#     plt.plot(vals, tan, label = 'Tan(x)')
#     plt.plot(vals, cot, label = 'Cot(x)')
#     plt.plot(vals, sec, label = 'Sec(x)')
#     plt.plot(vals, cosec, label = 'Cosec(x)')
#     plt.legend()
#     plt.show()

def q2():
    method = np.array(['A','B','C','D'])
    res1 = np.array([2,5,8,5])
    res2 = np.array([3,2,5,7])
    x1 = np.arange(len(res1))
    x2 = [x + 0.3 for x in x1]
    plt.bar(x1, res1, width=0.25, label='Result 1')
    plt.bar(x2, res2, width=0.25, label='Result 2')
    plt.xticks([x + 0.1 for x in x1], method)
    plt.legend()
    plt.show()

q2()

# data1 = {'A':2, 'B':5, 'C':8,'D':5}
# data2 = {'A':3, 'B':2, 'C':5,'D':7}
# courses = list(data1.keys())
# values1 = list(data1.values())
# values2=list(data2.values())  
# fig = plt.figure(figsize = (10, 5))
 
# # creating the bar plot
# plt.bar(courses, values1, color ='maroon',width = 0.4)
# plt.bar(courses, values2, color ='blue',width = 0.2)

 
# plt.xlabel("Method")
# plt.ylabel("Results")
# plt.title("Table")
# plt.show()