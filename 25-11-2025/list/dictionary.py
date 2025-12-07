#exercise 1 max dictionary
marks = {"A": 85, "B": 92, "C": 78, "D": 92}

max_value = None
for value in marks.values():
    if max_value is None or value > max_value:
        max_value = value
keys_with_max = []
for key, value in marks.items():
    if value == max_value:
        keys_with_max.append(key)
print(keys_with_max)

#exercise 2 swap key and values

data = {"a": 1, "b": 2, "c": 1}
inverted = {}
for key, value in data.items():
    if value in inverted:
        inverted[value].append(key)
    else:
        inverted[value] = [key]
print(inverted)

#exercise 3 merging two dictionaries

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = {}
for key, value in dict1.items():
    merged[key] = value
for key, value in dict2.items():
    if key in merged:
        merged[key] = [merged[key], value] if not isinstance(merged[key], list) else merged[key] + [value]
    else:
        merged[key] = value
print(merged)

#exercise4 removing all items

items = {"pen": 50, "book": 120, "bag": 90, "shoes": 250}
filtered_items = {}
for key, value in items.items():
    if value >= 100:
        filtered_items[key] = value
print( filtered_items)

