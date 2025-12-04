
#exercise 1

def count_vowels_consonants_digits(input_string):
    vowels = 'aeiouAEIOU'
    digits = '0123456789'

    num_vowels = 0
    num_consonants = 0
    num_digits = 0


    for char in input_string:
        if char.isdigit():
            num_digits += 1
        elif char.isalpha():  # Only consider alphabetic characters for vowels and consonants
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1

    return num_vowels, num_consonants, num_digits


input_string = input("Enter a string: ")

vowels, consonants, digits = count_vowels_consonants_digits(input_string)

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")

#Exercise 2
def word_frequencies(sentence):
    words = sentence.lower().split()
    word_count = {}
    for word in words:
        word = "".join(e for e in word if e.isalnum())  #
        if word:
            word_count[word] = word_count.get(word, 0) + 1

    return word_count

sentence = input("Enter a sentence: ")
result = word_frequencies(sentence)
print(result)

#exercise 3
class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        try:
            return a/b
        except ZeroDivisionError:
            print("Division by zero")
calc= Calculator()
print(calc.add(1,2))
print(calc.sub(3,4))
print(calc.mul(3,4))
print(calc.div(3,4))

#exercise 4
def second_highest(numbers):
    highest, second = float('-inf'), float('-inf')
    for num in numbers:
        if num > highest:
            second, highest = highest, num
        elif num > second and num != highest:
            second = num
    return second if second != float('-inf') else None


n = int(input("Enter the number of elements: "))
numbers = [int(input()) for _ in range(n)]
result = second_highest(numbers)
print(result)

#exercise 5
values = [int(input(f"Enter value {_ + 1}: ")) for _ in range(10)]
print("The values entered are:", values)
