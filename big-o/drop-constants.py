# drop constants:

def print_nums(n):
    for i in range(n):
        print(i)
    
    for j in range(n):
        print(j)

print_nums(10)

# this will run n + n times but we do not write the notation O(n + n) or O(2n), we simply write 

# O(n), we drop the constant no matter the number, even if it is 10 or whatever