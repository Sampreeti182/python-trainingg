nums =[0,3,0,5,7,0,9]
result=[]
for n in nums:
    if n!=0:
        result.append(n)
zero_count=nums.count(0)
result+=[0]*zero_count
print(result)
