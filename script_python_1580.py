# This is a simple Python script with random content for basic calculations
import random
# Generate two random numbers
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
# Basic calculations
print(f'{num1} + {num2} = {num1 + num2}')
print(f'{num1} - {num2} = {num1 - num2}')
print(f'{num1} * {num2} = {num1 * num2}')
print(f'{num1} / {num2} = {num1 / num2}' if num2 != 0 else 'Error: Division by zero')
