# constant time complexity
n = 1
print(n)

# linear time complexity
for i in range(0,n):
    print("Hello")

# quadratic time complexity
for i in range(0,n):
    for j in range(0,n):
        print("Hello")

# cubic time complexity
for i in range(0,n):
    for j in range(0,n):
        for k in range(0,n):
            print("Hello")

# logerithmic time complexity
while n >= 1:
    print("Hello")
    n = n//2

# logerithmic time complexity
while n <=10:
    print("Hello")
    n = n * 2