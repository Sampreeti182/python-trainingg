#exercise  1
def remove_duplicates(prices):

    unique_prices = []
    for price in prices:
        if price not in unique_prices:
            unique_prices.append(price)
    return unique_prices
prices = [1, 2, 3, 4, 5, 6, 7, 8, 9,7,2,8,0.5,0.3,0.5 ,10]
unique_prices = remove_duplicates(prices)
print(unique_prices)

#exercise 2
def merge_list_to_dict(list1,list2):
    return dict(zip(list1,list2))
list1=["Sampreeti","Tania","Robert"]
list2=[23,22,30]
result=merge_list_to_dict(list1,list2)
print(result)

#exercise 3
def top_3_students(marks_dict):
    students = list(marks_dict.items())
    students.sort(key=lambda x: x[1], reverse=True)

    top_3 = students[:3]

    return top_3

students_marks = {
    "Sampreeti": 99,
    "Tania": 92,
    "Charlie": 88,
    "David": 75,
    "Eveline": 95,
    "Frank": 89
}

top_students = top_3_students(students_marks)
print("Top 3 students:")
for student, marks in top_students:
    print(f"{student}: {marks}")

#exercise 4
def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened_list = flatten_list(nested_list)

print("Flattened list:", flattened_list)

#exercise 5
def common_elements(set1, set2,set3):
    return set1&set2&set3

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set3 = {5, 6, 7, 8, 9}

common = common_elements(set1, set2, set3)

print("Common elements:", common)

#exercise 6
def convert_to_dict(tuples):

    keys = [key for key, value in tuples]
    if len(keys) == len(set(keys)):
        return dict(tuples)
    else:
        return "Error: Keys are not unique"
tuples = [('a', 1), ('b', 2), ('a', 3)]
print(convert_to_dict(tuples))

tuples = [('a', 1), ('b', 2), ('c', 3)]
print(convert_to_dict(tuples))

#exercise 7
def unique_names(names_tuple):
    return tuple(set(names_tuple))
names = ('Alice', 'Bob', 'Alice', 'Charlie', 'Bob')
print(unique_names(names))

#exercise 8
def reverse_alternate_elements(lst):

    for i in range(1, len(lst), 2):
        lst[i] = lst[i][::-1]
    return lst
lst = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(reverse_alternate_elements(lst))

#exercise 9
def filter_employees_by_salary(employees):
    return {name: salary for name, salary in employees.items() if salary > 60000}

# Example usage
employees = {
    'John': 50000,
    'Jane': 75000,
    'Tom': 65000,
    'Lucy': 40000
}

print(filter_employees_by_salary(employees))

#exercise 10
def combine_and_sum_dicts(dict1, dict2):

    combined = dict1.copy()
    for key, value in dict2.items():
        if key in combined:
            combined[key] += value
        else:
            combined[key] = value
    return combined
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'a': 5, 'b': 10, 'd': 15}
print(combine_and_sum_dicts(dict1, dict2))
