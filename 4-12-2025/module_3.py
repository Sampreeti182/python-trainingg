#exercise 1
class Student:
     def __init__(self, student_id, name, marks):
         self.student_id = student_id
         self.name = name
         self.marks = marks

     def calculate_grade(self):

         if self.marks >= 90:
             return "A+"
         elif self.marks >= 80:
             return "A"
         elif self.marks >= 70:
             return "B"
         elif self.marks >= 60:
             return "C"
         elif self.marks >= 50:
             return "D"
         else:
             return "F"

     def __str__(self):

         return f"Student ID: {self.student_id}, Name: {self.name}, Marks: {self.marks}, Grade: {self.calculate_grade()}"

student1 = Student(101, "Alice", 92)
student2 = Student(102, "Bob", 75)
student3 = Student(103, "Charlie", 48)
print(student1)
print(student2)
print(student3)

#exercise 2
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_details(self):
        return f"Product Name: {self.name}, Price: ${self.price}"
class ElectronicProduct(Product):
    def __init__(self, name, price, warranty_years):
        super().__init__(name, price)
        self.warranty_years = warranty_years

    def get_details(self):
        return f"{super().get_details()}, Warranty: {self.warranty_years} years"

tv = ElectronicProduct("Smart TV", 500, 2)
print(tv.get_details())

#exercise 3
class Payment:
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses must implement this method.")

class CreditCard(Payment):
    def process_payment(self, amount):
        return f"Payment of ${amount} processed through Credit Card."
class UPI(Payment):
    def process_payment(self, amount):
        return f"Payment of ${amount} processed through UPI."
credit_card_payment = CreditCard()
print(credit_card_payment.process_payment(100))

upi_payment = UPI()
print(upi_payment.process_payment(200))

#exercise 4
class Vehicle:
    def max_speed(self):
        return "The max speed of the vehicle is not defined."

class Car(Vehicle):
    def max_speed(self):
        return "The max speed of the car is 150 km/h."

class Bike(Vehicle):
    def max_speed(self):
        return "The max speed of the bike is 120 km/h."

car = Car()
print(car.max_speed())

bike = Bike()
print(bike.max_speed())

#exercise 5
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return BankAccount(self.balance + other.balance)

    def __str__(self):
        return f"Bank Account Balance: ${self.balance}"

account1 = BankAccount(1000)
account2 = BankAccount(500)

total_balance = account1 + account2
print(total_balance)

#exercise 6
class shoppingcart:
    def __init__(self):
        self.items = []
    def add_item(self,name,price):
        self.items.append((name,price))
        print(name,"added to cart")
    def remove_item(self,name):
        for item in self.items:
            if item[0]==name:
                self.items.remove(item)
                print(name,"removed from cart")
                return
        print(name,"not in cart")
    def total_cost(self):
        total=0
        for item in self.items:
            total+=item[1]
        return total
    def apply_discount(self,percent):
        total= self.total_cost()
        discount_amount=total*(percent/100)
        final_price=total-discount_amount
        return final_price
    def display_items(self):
        if not self.items:
            print("No items added to cart")
            return
        print("Items added to cart:")
        for name,price in self.items:
            print(name,"=",price)
cart=shoppingcart()
cart.add_item("Milk",100)
cart.add_item("carrot",60)
print()
cart.display_items()
print()
print("total cost:",cart.total_cost())
print("final price:",cart.apply_discount(100))
print()
cart.remove_item("carrot")
cart.display_items()

#exercise 7
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}"

class Admin(User):
    def __init__(self, username, email, admin_level):
        super().__init__(username, email)
        self.admin_level = admin_level


    def delete_user(self, user, user_list):
        if user in user_list:
            user_list.remove(user)
            return f"User {user.username} has been deleted."
        else:
            return "User not found."

user1 = User("john_doe", "john@example.com")
user2 = User("jane_doe", "jane@example.com")

admin = Admin("admin_user", "admin@example.com", "SuperAdmin")
users = [user1, user2]
print("Before deletion:")
for user in users:
    print(user)

print(admin.delete_user(user1, users))

print("\nAfter deletion:")
for user in users:
    print(user)
