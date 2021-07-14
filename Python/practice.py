num = 1
num01 = 2
num_01 = 3
# num$01 = 4
# num-01 = 5
# 01num = 06

print(num)
print(num01)
print(num_01)
# print(num$01)
# print(num-01)
# print(01num)

NUM = 1
Num = 2

print(NUM)
print(Num)

# return = 10

# print(return)

num01 = 123
num02 = 1.23

print(num01)
print(num02)
print(type(num01))
print(type(num02))

string_a ="Hello,World!"

print(string_a)
print(type(string_a))

a = 10
b = 1

bool01 = (a > b)

print(bool01)
print(type(bool01))

bool01 = (a < b)

print(bool01)
print(type(bool01))

a = ["sato","suzuki","takahashi"]

print(a[0])
print(a[1])
print(a[2])

a[1] = "tanaka"

print(a[0])
print(a[1])
print(a[2])

a = [["sato","suzuki"],["takahashi","tanaka"]]

print(a[0][0])
print(a[0][1])
print(a[1][0])
print(a[1][1])

x = 10
y = 2

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)

x = 10
y = 2 
z = 10

print(x > y)
print(x < y)
print(x <= y)
print(x >= z)
print(x == y)
print(x != y)

x = 8
y = 3

print(x >= 5 and x <= 10)
print(y >= 5 and y <= 10)
print(x == 3 or y == 3)
print(x == 1 or y == 1)

x = 8
y = 12
z = 20

x += 10
z += y

print(x)
print(z)

age = 22

if age >= 20:
    print("adult")

age = 18

if age >= 20:
    print("adult")

age = 18

if age >= 20:
    print("adult")
else:
    print("child")

age = 0

if age >= 20:
    print("adult")
elif age == 0:
    print("baby")
else:
    print("child")

for i in range (5):
    print(i)

for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 3:
        continue
    print(i)

for i in range(3):
    for j in range(3):
        print(i, j, sep = "-")

arr = [2, 4, 6, 8, 10]
for i in arr:
    print(i)

arr = [2, 4, 6, 8, 10]
sum = 0
for i in arr:
    sum += i
print(sum)
