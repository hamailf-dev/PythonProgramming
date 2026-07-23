print("=== 7.1 Basic Decorator ===")
def timer_decorator(func):
    def wrapper():
        print("Function shuru ho rahi hai...")
        func()
        print("Function khatam ho gayi")
    return wrapper

@timer_decorator
def greet():
    print("Hello, Welcome!")

greet()

print("\n=== 7.2 Decorator with arguments ===")
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    print(f"Hello {name}")

say_hello("Ali")