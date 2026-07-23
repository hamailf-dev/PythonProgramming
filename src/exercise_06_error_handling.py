# 06 · Error Handling
print("\n--- Exercise 6: Error Handling ---")

# 6.1 — Basic try/except
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Please enter numbers only"

print("6.1 10/2 =", safe_divide(10, 2))
print("6.1 10/0 =", safe_divide(10, 0))
print("6.1 10/'a' =", safe_divide(10, 'a'))

# 6.2 — try/except/finally
def read_file(filename):
    try:
        f = open(filename, 'r')
        content = f.read()
        return content
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    finally:
        print("6.2 File operation attempted")

print("6.2", read_file("data.txt"))

# 6.3 — Custom exception
class NegativeValueError(Exception):
    pass

def set_age(age):
    if age < 0:
        raise NegativeValueError("Age cannot be negative")
    return age

try:
    print("6.3 Age:", set_age(25))
    print("6.3 Age:", set_age(-5))
except NegativeValueError as e:
    print("6.3", e)

print("\n--- Exercise 6 Complete ---")