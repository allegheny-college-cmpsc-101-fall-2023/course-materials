"""Warmup questions."""
# what error will appear when you run this code?

print(f"displaying the square of numbers in this list: {[i for i in range(10)]}")
print([square(i) for i in range(10)])

def square(x: int) -> int:
    return x*x

# What can you do to fix this error?
