nums = [23,89,12,78,55,42]
first = float('-inf')
second = float('-inf')
for x in nums:

   if x> first:
       second = first
       first = x

   elif first>x>second:
       second = x
print("Second largest:", second)
