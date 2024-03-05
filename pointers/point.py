# practicing with pointers:

num1 = 14    # same place in memory and if I change one they will no longer point to the same place in memory
num2 = num1

def memory(x, y, z=1):
    print('num1 is stored at %d' % id(x))
    print('num2 is stored at %d' % id(y))

# print(type(id(num1)))

num2 = 4    # this does not change num1 as integers are immutable

memory(num1, num2)

dict1 = {4: 8, 12: 16}

dict2 = dict1

print()

print(id(dict1), id(dict2))

dict2 = {5: 7, 9: 17}

print()

print(id(dict1), id(dict2))

