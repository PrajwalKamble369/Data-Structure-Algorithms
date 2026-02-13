import numpy as np

arr = np.array([1,2,3,4],dtype= float)
print(arr)

val = np.linspace(10,20,5)
val0 = np.arange(10,20,2)
val1 = np.logspace(10,20,2)
val2 = np.zeros(10)
val3 = np.ones(3)
val4 = np.full(10,5)

print()

for x in arr:
    print(x,end=" ")

print()

for i in val:
    print(i,end=" ")

print()

for i in val0:
    print(i,end=" ")

print()

for i in val1:
    print(i,end=" ")

print()

for i in val2:
    print(i,end=" ")


print()

for i in val3:
    print(i,end=" ")

print()

for i in val4:
    print(i,end=" ")
print()

zero = np.array(10)
print(zero)

one = np.array([1,2,3,4])
print(one)

two = np.array([[1,2],[3,4]])
print(two)

three = np.array([[[1,2],[3,4],[5,6]]])
print(three)

s = "I love AI"
s_n = []

for i in s:
    if i == " ":
        continue
    else:
        s_n.append(i)
print(s_n)
for i in s_n:
    print(s_n[-1:0])