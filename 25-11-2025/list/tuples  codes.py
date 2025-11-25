#seperating two tuples
tup = (1,"sampreeti",4, "tulips",6,"leaf")
nums=[]
strings=[]
for i in tup:
    if type(i)==int or type(i)==float:
        nums.append(i)
    else:
        strings.append(i)
nums=tuple(nums)
strings=tuple(strings)
print(nums)
print(strings)

#increasing tuple
t=(1,3,7,8)
increasing=True
for i in range(len(t)-1):
    if t[i]>=t[i+1]:
        increasing=False
        break
if increasing:
    print(" strictly increasing")
else:
    print(" not strictly increasing")

#reverse tuple


words = ("python", "cloud", "data")
reversed_words = tuple(word[::-1] for word in words)

print("Original Tuple:", words)
print("Reversed Tuple:", reversed_words)

#index of a tuple

data = (10, 20, 30, 20, 40, 20, 50)
value = 20
positions = []
for i in range(len(data)):
    if data[i] == value:
        positions.append(i)
print(positions)

#tuple using recursion

def print_integers(t):
    for item in t:
        if isinstance(item, int):
            print(item)
        elif isinstance(item, tuple):
            print_integers(item)
data = (10, (20, 30), (40, (50, 60)))
print_integers(data)
