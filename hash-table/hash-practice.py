# a practice file for hash tables:

number = 7

x = [None] * number

print(x)  # [None, None, None, None, None, None, None]

# enumerate:

y = enumerate(x)


# print(list(y))  # without list it will display <enumerate object at 0x7fe07e67af80>

# [(0, None), (1, None), (2, None), (3, None), (4, None), (5, None), (6, None)]  # the output from 2 lines above 

# for a, b in y:
#     print(a, b)

z = sorted([(a, b) for a, b in y], reverse=True)

print(z)

# interview problem, take 2 lists and find out if they share a common element:



a = [1, 2, 5]

b = [3, 4, 5]

# this is the slow and naive way of doing it, it will work but it is O(n**2), very slow

c = []

for i in a:
    for j in b:
        if i == j:
            c.append(i)

print(c)

# make the above a function, we will create a more efficient algorithm for this in ht-interview.py 

def match(l1, l2):
    for i in l1:
        for j in l2:
            if i == j:
                return True
    return False 

print()  

print(match(a, b))