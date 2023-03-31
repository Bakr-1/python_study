#!/usr/bin/env python
# coding: utf-8

# In[1]:


X = [1, 2.3, 3.1, 4.8, 5.6, 6.3]

SizeX = len(X)
SumX = sum(X)
SumXS = (1 + 2.3 * 2.3 + 3.1 * 3.1 + 4.8 * 4.8 + 5.6 * 5.6 + 6.3 * 6.3)

A1 = [SizeX, SumX]
A2 = [SumX, SumXS]
#print(A1)
#print(A2)

Det = 1 / ((len(X) * SumXS) - (SumX * SumX))

SumX = -SumX
inverse = [Det * SumXS, Det * SumX,
           Det * SumX, Det * SizeX]


#print(inverse)
e = []
b = []
index = 0
for i in X:
    e.append(inverse[0] + inverse[1] * i)
    b.append(inverse[2] + inverse[3] * i)
    index = index + 1

q = []
w = []
index=0
y = [2.6, 2.8, 3.1, 4.7, 5.1, 5.3]

#for i in y:
#    q.append(e[0] * i+e[1] * i+e[2] * i+e[3] * i+e[4] * i+e[5] * i)
 #   w.append(b[0] * i+b[1] * i+b[2] * i+b[3] * i+b[4] * i+b[5] * i)
 #   index = index + 1
#print(q)
#print(w)
#print(e)
#print(b)

