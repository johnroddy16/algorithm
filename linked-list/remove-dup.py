# practicing removing duplicates from a list:

nums = [10, 20, 20, 30, 40, 40, 40, 60, 80]
x = set(nums)
print(x)
y = list(x)
y.sort()
print(y)

print()

num_list = []

removed = []

index = 0

for i in nums:
    if index == 0:
        num_list.append(i)
        index += 1
        continue 
    if nums[index] == nums[index-1]:
        removed.append(i)
        index += 1 
        continue
    else:
        num_list.append(i)
        index += 1


print(num_list, '\n', removed)