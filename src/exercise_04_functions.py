# 04 · Functions
print("\n--- Exercise 4: Functions ---")

def is_even(n):
    return n % 2 == 0

print("4.1 is_even(10):", is_even(10))
print("4.1 is_even(7):", is_even(7))

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print("4.2", greet("Ada"))
print("4.2", greet("Sam", "Hi"))

def my_max(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

print("4.3 my_max([3, 9, 2, 7]):", my_max([3, 9, 2, 7]))

print("\n--- Exercise 4 Complete ---")