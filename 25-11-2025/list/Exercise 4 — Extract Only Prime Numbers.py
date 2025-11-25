nums=[10,11,12,13,17,20,23]
prime_list=[]
for n in nums:
    if n >1 :
        for i in range(2,n):
            if n %i==0:
                break
            else:
                prime_list.append(n)

print(prime_list)
