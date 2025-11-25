nums = ['a','b','c','d','e']
first = nums.pop(0)
last = nums.pop(-1)
nums.insert(0,last)
nums.append(first)
print(nums)
