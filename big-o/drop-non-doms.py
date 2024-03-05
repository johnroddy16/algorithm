# drop non-dominants as another way to simplify:

def print_nums(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

    for k in range(n):
        print(k)

print_nums(10)


# this ran O(n**2) + O(n) times so we could write O(n**2 + n) but we drop the non-dominant portion and simply write
# O(n**2), as a percentage of operations the O(n) is not significant