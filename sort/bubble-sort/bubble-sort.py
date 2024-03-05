# bubble-sort:

# with bubble sort we bubble up the largest item in a list:

for i in range(6, 0, -1):
    print(i)  
    
# 6
# 5
# 4
# 3
# 2
# 1
    
def bubble_sort(l):
    for i in range(len(l) - 1, 0, -1):  # for i in range 7 6 5 4 3 2 1 
        for j in range(i):  # for j in 0 1 2 3 4 5 7 first time thru since i will be 6 
            if l[j] > l[j + 1]:  # if l[0] > l[1] it is in this case 
                temp = l[j]  # temp = 18
                l[j] = l[j + 1]  # l[0] = 11
                l[j + 1] = temp  # l[1] = 18, which was held in temp, we have bubble 18 up one spot 

    return l 

nums = [18, 11, 14, 12, 4, 7, 2, 1]

print(bubble_sort(nums))  # [1, 2, 4, 7, 11, 12, 14, 18], seems to work fine 