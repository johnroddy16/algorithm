# different terms for inputs, sometimes asked at interviews as a gotcha ?:

def print_nums(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)            # O(n) since we drop constants and do not write O(2n) or O(n + n)


def print_items(a, b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)           # we have made a change and we cannot simply write O(n) by dropping a constant

                           # a and b are 2 different things so we cannot write them both as n

                           # we have to submit to the fact that we have 2 different terms
                           # and write that we have O(a) + O(b), written O(a + b) and that is as simplified as we get

# with nested loops:

def print_items(a, b):
    for i in range(a):
        for j in range(b):
            print(i, j) 

# here we can only simplify to O(a * b) because the loops are nested