def factorial(num):
    fact = 1
    while num > 1:
        fact *= num
        num -= 1
    return fact 
n = 5
print(f"The factorial of {n} is {factorial(n)}")