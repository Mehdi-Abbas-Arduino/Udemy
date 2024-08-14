def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
num = factorial(int(input("Enter the number = ")))
print(f"Number is {num}")
'''Fibonacci Series'''
# F0 = 1
# F1 = 1
# Fn = Fn-1 + fn-2

def fibonacci(n):
    if n==0:
        return 0
    elif (n==1):
        return 1
    else:
        fib = fibonacci(n-1) + fibonacci(n-2)
        return fib
    
print(fibonacci(3))