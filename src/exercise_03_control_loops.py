# 03 · Control flow & loops
print("\n--- Exercise 3: Control Flow & Loops ---")

# 3.1 — FizzBuzz
print("\n3.1 FizzBuzz 1-20:")
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 3.2 — Sum the evens
print("\n3.2 Sum of evens 1-100:")
total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print("Loop method:", total)

# One-line list comprehension
total_comp = sum([i for i in range(1, 101) if i % 2 == 0])
print("Comprehension method:", total_comp)

# 3.3 — Comprehension practice
words = ["hi", "hello", "hey", "howdy"]
long_words_upper = [word.upper() for word in words if len(word) > 3]
print("\n3.3 Words > 3 chars UPPERCASE:", long_words_upper)

print("\n--- Exercise 3 Complete ---")