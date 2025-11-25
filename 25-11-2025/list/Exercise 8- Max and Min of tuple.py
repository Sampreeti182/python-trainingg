numbers=[33,20,30,60,50]
max=numbers[0]
min=numbers[0]
for n in numbers:
    if n > max:
        max=n
    if n < min:
        min=n
print("maximum is",max)
print("minimum is",min)
