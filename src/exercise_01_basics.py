# Exercise 1: Basics & Variables
print("Hello, my name is Hamail")
print("Welcome to my Python Programming practice repo!")

name = "Hamail"          # str
age = 20                 # int
height = 5.1             # float
is_student = True        # bool

print("\n--- Variables ---")
print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("Height:", height, "| Type:", type(height))
print("Is Student:", is_student, "| Type:", type(is_student))

age_str = str(age)       # Convert int to str
print("\nAge as string:", age_str, "| Type:", type(age_str))

height_int = int(height) # Convert float to int. 5.1 becomes 5
print("Height as int:", height_int, "| Type:", type(height_int))

print("\n--- Exercise 1 Complete ---")