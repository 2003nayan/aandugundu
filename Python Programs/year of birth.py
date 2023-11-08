from datetime import datetime

name = input("Enter your name: ")
age = input("Enter your age: ")

age = int(age)

current_year = datetime.now().year

year_of_birth = current_year - age

print("Your name is ", name," and your year of birth is ", year_of_birth )