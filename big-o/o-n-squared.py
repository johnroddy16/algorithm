# O(n**2):

# this will occur in a nested loop:

def print_nums(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

print_nums(10)

# will run n ** 2 times, or n * n times due to the nested loop

# O(n**2) will be much steeper on a graph and will not be as good in time complexity as O(n)