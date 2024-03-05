# creating a class called cookie and creating some objects:

class Cookie:
    def __init__(self, color='blue'):
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color


cookie_one = Cookie()

x = cookie_one.color
print(x)


cookie_two = Cookie('green')
print(cookie_two)
print(cookie_two.color)

y = cookie_two.get_color()
print(y)

cookie_one.set_color('pink')
print(cookie_one.color)

print('cookie one is %s' % cookie_one.get_color())
print('cookie two is %s' % cookie_two.get_color())