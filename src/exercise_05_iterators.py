print("=== 5.1 Manual walk ===")
letters = ["a", "b", "c"]
it = iter(letters)

print(next(it))  # a
print(next(it))  # b
print(next(it))  # c

try:
    print(next(it))  # 4th call - will cause error
except StopIteration:
    print("StopIteration: No more items to get")

print("\n=== 5.2 Rebuild the for-loop ===")
colors = ["red", "green", "blue"]
it = iter(colors)

while True:
    try:
        item = next(it)
        print(item)
    except StopIteration:
        break