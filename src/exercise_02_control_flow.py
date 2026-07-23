# Exercise 2: Control Flow
print("\n--- Exercise 2: Control Flow ---")

# 2.1 if / elif / else
age = 20
if age < 18:
    print("You are a minor")
elif age >= 18 and age < 60:
    print("You are an adult")
else:
    print("You are a senior")

# 2.2 for loop
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print("Number:", i)

# 2.3 while loop
print("\nCountdown:")
count = 3
while count > 0:
    print(count)
    count = count - 1
print("Go!")

# 2.4 Loop with list
names = ["Ali", "Sara", "Ahmad"]
print("\nStudent List:")
for name in names:
    print("Hello,", name)

print("\n--- Exercise 2 Complete ---")