#union but not intersection
s={1,2,3,4}
r={4,5,6,7}

union_set = s.union(s)
intersection_set = s.intersection(r)
result = union_set - intersection_set
print("Union but not Intersection:", result)

#converting a tuple in a set

t = [3, 1, 2, 3, 2, 4, 1, 5, 4, 6, 6]

# Create an empty set to track seen elements
seen = set()
# Create an empty list for the result
result = []

# Iterate through the original list
for item in t:
    if item not in seen:
        seen.add(item)      # Add to set
        result.append(item)
print(result)

#pairs summing up to a target number
numbers= {2,4,6,8,10}
target=12
numbers= list(numbers)
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]+numbers[j] == target:
            print(numbers[i],numbers[j])

#disjoint sets

set1 = {1, 2, 3, 4}
set2 = {5, 6, 7}
disjoint = True
for item in set1:
    if item in set2:
        disjoint = False
        break
if disjoint:
    print("disjoint")
else:
    print("not disjoint")

#unique characters

words = ["python", "cloud", "data"]
unique_chars = set()
for word in words:
    unique_chars.update(word)
result = sorted(unique_chars)
print(result)
