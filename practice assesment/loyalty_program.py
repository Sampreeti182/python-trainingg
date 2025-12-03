class Customer:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def is_eligible_for_loyalty_program(self):
        if self.age > 25:
            return True
        else:
            return False
customer = Customer("Sampreeti", 26, "Kolkata")
eligibility = customer.is_eligible_for_loyalty_program()
if eligibility:
    print(f"{customer.name} is eligible for the loyalty program.")
else:
    print(f"{customer.name} is not eligible for the loyalty program.")