nums = [5,2,7,5,9,5,3]
value = 5
list=[]
for i in range(len(nums)):
    if nums[i]==value:
        list.append(i)
print(list)
