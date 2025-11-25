#rearrange negative numbers
nums=[1,2,-9,-4,6,8,-3]
pos=[]
neg=[]
for n in nums:
    if n <0:
        neg.append(n)
    else:
        pos.append(n)
res=neg+pos
print(res)

#elements appearing more than once
nums=[1,2,3,2,4,1,5,1]
list=[]
for n in nums:
    if nums.count(n)>1 and n not in list:
        list.append(n)
print(list)

#Roatating a list
nums=[1,2,3,2,4,1,5,]
n=2
for i in range(n):
    first = nums[0]
    for i in range(len(nums)-1):
        nums[i]=nums[i+1]
    nums[-1]=first
print(nums)

#srtings length less than 3
list=["sampreeti","rose","bus","a"]
list_2=[]
for i in list:
    if len(i)>=3:
        list_2.append(i)
print(list_2)

#nested list
nums=[[1,2],[3,4],[5,6]]
flat=[]
for i in nums:
    if type(i)==list:
        for x in item:
            flat.append(x)
        else:
            flat.append(i)
print(flat)
