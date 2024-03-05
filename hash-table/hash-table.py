# we will create a hash table class:






class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def hash(self, key):  # O(1)
        h = 0
        for l in key:
            h = (h + ord(l) * 11) % len(self.data_map)  # this will create a random number to associate with the key  
        return h 
    
    def print_table(self):
        for a, b in enumerate(self.data_map):  # see hash-practice for examples with enumerate
            print(f'{a}: {b}')
    
    def set_item(self, key, value):  # O(1)
        index = self.hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):  # O(1)
        # pass
        # will tackle the get_item method next:
        index = self.hash(key)
        if self.data_map[index]:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None 
    
    # next we will create a key method that will return a list of all keys, in this case what we have in inventory 
    # to do that we will need to iterate thru the data map with a nested for loop and return anything that is there, let us see
    # if i can do myself: i could not this time but i'll get the next one

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i]:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys 





ht = HashTable()

# ht.hash('table')  # this does not do anything

ht.set_item('bolts', 1400) 

ht.set_item('washers', 106)

ht.set_item('screws', 4618)

print(ht.get_item('bolts'))  # 1400

# print(ht.get_item('trees'))  # None

# print(ht.get_item('screws'))  # 4618

# print(ht.get_item('washers'))  # 106

print()

print(ht.keys())

print()  

ht.print_table()