# O(1):

def add_nums(n):
    return n + n

x = add_nums(4)

print(x)

# no matter the number n there is only one operation that will run, and even if we were returning n + n + n we would still 
# write O(1)


# O(1) is also called constant time

# on a graph O(1) will be a stright line on the x axis, very time efficient