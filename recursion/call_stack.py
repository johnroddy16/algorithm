# practicing with a call stack:



def funcone():
    functwo()
    print('hello one')

def functwo():
    functhree()
    print('hello two')

def functhree():
    print('hello three')

funcone()

# will output:

# hello three
# hello two
# hello one