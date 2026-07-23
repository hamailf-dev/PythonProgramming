# 07 · Modules & Packages
print("\n--- Exercise 7: Modules & Packages ---")

# 7.1 — Import from our own module
from utils.math_tools import add, multiply, power

print("7.1 add(5, 3) =", add(5, 3))
print("7.1 multiply(4, 7) =", multiply(4, 7))
print("7.1 power(2, 5) =", power(2, 5))

# 7.2 — Import standard library
import math
import random
from datetime import datetime

print("7.2 sqrt(16) =", math.sqrt(16))
print("7.2 random number:", random.randint(1, 10))
print("7.2 Today:", datetime.now().strftime("%Y-%m-%d"))

# 7.3 — Import with alias
import utils.math_tools as mt

print("7.3 Using alias: mt.add(10, 20) =", mt.add(10, 20))

print("\n--- Exercise 7 Complete ---")