print("=== 6.1 countdown generator ===")
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(5):
    print(x)

print("\n=== 6.2 squares generator ===")
def squares(n):
    for i in range(1, n + 1):
        yield i * i

for x in squares(5):
    print(x)