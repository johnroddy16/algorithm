# a linked list is kind of like nested dictionaries:

head = {
    'value': 24,
    'next': {
        'value': 32,
        'next': {
            'value': 44,
            'next': {
                'value': 56,
                'next': {
                    'value': 68,
                    'next': {
                        'value': 84,
                        'next': None 
                    }
                }
            }
        }
    }
}

print(head['next']['next']['next']['value'])  # 56 
print(head['next']['next']['next']['next']['value'])  # 68
print(head['next']['next']['value'])  # 44


# if we were using a linked list object we would write the following to take the place of the line 25:

# print(my_linked_list.head.next.next.value)  # my_linked_list is an arbitrary name