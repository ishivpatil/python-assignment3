#Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
#recursion factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
number = int(input("Enter the number: "))
print(f"The factorial of {number} is {factorial(number)}")

#Asks the user for a number as input.
#module
import math
number = float(input("Enter the number: "))
sqrt = math.sqrt(number)
log_result = math.log(number)
sine_result = math.sin(number)
print(f"sqrt({number}) = {math.sqrt(number)}")
print(f"log_result({number}) = {log_result}")
print(f"sine_result({number}) = {sine_result}")
