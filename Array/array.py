from array import *

val = array("i",[1,2,3,4,5,6,7,8,9])

for i in range(0,len(val)):
    print(val[i],end=" ")

print("\n")

for x in val:
    print(x,end=",")

print("\n")

print(val.typecode)

val.reverse()
for i in val:
    print(i,end=" ")

print("\n")

val.insert(1,50)
val.append(100)
val[2] = 200

copy_array = array(val.typecode,(x*3 for x in val))
copy_array.pop(3)
copy_array.remove(15)

for i in val:
    print(i,end=" ")

print("\n")

for i in copy_array:
    print(i,end="|")

print("\n")

val = array("i",[0,1,2,3,4,5,6,7,8,9])
abc = val[2:5]

for i in val:
    print(i,end="|")

print("\n")

for i in abc:
    print(i,end="|")

print("\n")

val = array("i",[0,1,2,3,4,5,6,7,8,9])
abc = val[2:-3]

for i in val:
    print(i,end="|")

print("\n")

for i in abc:
    print(i,end="|")

print("\n")

val = array("i",[0,1,2,3,4,5,6,7,8,9])
abc = val[::-1]
for i in val:
    print(i,end="|")

print("\n")

for i in abc:
    print(i,end="|")


arr = array("i",[])

n = int(input("enter a number: "))

for i in range(0,n):
    arr.append(int(input("enter next input: ")))

for i in arr:
    print(i,end=" ")
print("\n")

i = arr.index(45)
print(i)
