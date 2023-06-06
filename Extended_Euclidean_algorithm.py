def gcdExtended(a, b, x, y):
    # Base Case
    if a == 0:
        x = 0
        y = 1
        return b
    x1 = 1
    y1 = 1  # storing the result
    gcd = gcdExtended(b % a, a, x1, y1)
    # Update x and y with previous calculated values
    x = y1 - (b/a) * x1
    y = x1
    return gcd


x = 1
y = 1
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
g = gcdExtended(a, b, x, y)
print("gcd of ", a, "&", b, " is = ", g)
