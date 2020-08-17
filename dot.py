import numpy as np
A=np.zeros((32,32))
A[:][:]=np.arange(32*32).reshape(32,32)
B=A
print(np.dot(A,B))
