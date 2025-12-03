class Student:
    def __init__(self, name, subject1, subject2, subject3):
        self.name = name
        self.subject1, self.subject2, self.subject3 = subject1, subject2, subject3

    def total(self):
        return self.subject1 + self.subject2 + self.subject3

    def percentage(self):
        return (self.total() / 300) * 100

    def grade(self):
        percentage = self.percentage()
        if percentage >= 90: return 'A'
        elif percentage >= 75: return 'B'
        elif percentage >= 60: return 'C'
        elif percentage >= 40: return 'D'

student = Student("Sampreeti", 85, 78, 92)
print(f"{student.name}: Total={student.total()}/300, Percentage={student.percentage():.2f}%, Grade={student.grade()}")