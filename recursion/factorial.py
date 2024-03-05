# we will practice recursion with factorials:

# a factorial is written 4!, which would be in this case 4 * 3 * 2 * 1 = 24, so 4! = 24 

# you could say that 4! = 4 * 3!, which would be the same thing 

def factorial(n):
    if n == 1:  # our base case 
        return 1  
    return n * factorial(n-1)