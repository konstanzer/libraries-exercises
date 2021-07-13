import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

#questions lol
print(a)
print("pos/neg")
print(4)
print(5)
print(3)
print(10)
print('moments')
print(np.mean(pow(a,2)))
print(np.std(pow(a,2)))
print('centering')
print(np.mean(a))
print(a-np.mean(a))
print(np.mean(a-np.mean(a)))
print("z-scores")
def Z(x): return((x-np.mean(x))/np.std(x))
print(Z(a))