#  Write a Python program to get the Fibonacci series of given range.  
def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

terms = int(input("Enter the number of terms for Fibonacci series: "))

if terms <= 0:
    print("Please enter a positive integer.")
else:
    
     print(f"The Fibonacci series for {terms} terms is: {fibonacci_series(terms)}")