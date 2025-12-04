#ex1
with open("sample.txt", "w") as f:
    f.write("Welcome to my notes. \n")
    f.write("You are doing great.\n")
    f.write("This note was made on 27th november. \n")
    f.write("Little steps make big progress \n")
    f.write("Have a nice day! \n")

with open("sample.txt") as f:
    text = f.read()

chars = len(text)
words = len(text.split())
lines = text.count("\n") + 1
print("characters:", chars)
print("words:", words)
print("lines:", lines)
#ex2
import csv

employees = [
    {"id": i, "name": f"Emp{i}", "salary": 30000 + i * 1000}
    for i in range(1, 21)
]
with open("employees.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name", "salary"])
    writer.writeheader()
    writer.writerows(employees)

with open("employees.csv") as f:
    reader = csv.DictReader(f)
    data = list(reader)

print(data)
#ex3
from datetime import datetime
def log(message):
  with open("log.txt", "a") as f:
      f.write(f"{datetime.now()} - {message}\n")
  with open("log.txt", "r") as f:
      print(f.read())
log("program started")
log("user logged in")
#ex4
import json

product = [
    {"id": 1, "name": "Chocolate Cake", "price": 5000},
    {"id": 2, "name": "laptop", "price": 90000},
    {"id": 3, "name": "Apple", "price": 100},
    {"id": 4, "name": "Banana", "price": 200}
]

with open("product.json", "w") as f:
    json.dump(product, f, indent=4)
with open("product.json") as f:
    product = json.load(f)
for p in product:
    p["discount_price"] = round(p["price"] * 0.9, 2)
with open("product.json", "w") as f:
    json.dump(product, f, indent=4)
print("updated products saved to json")
#ex5
with open("bigfile.txt", "w") as f:
    f.write("Welcome to my notes. \n")

    f.write("You are doing great.\n")

    f.write("This note was made on 27th november. \n")

    f.write("Little steps make big progress \n")

    f.write("Have a nice day! \n")

with open("bigfile.txt") as f:
    lines = f.readlines()

mid = len(lines) // 2

with open("part1.txt", "w") as f1:
    f1.writelines(lines[:mid])

with open("part2.txt", "w") as f2:
    f2.writelines(lines[mid:])

print("files part 1 and part 2 have been made")
