#Functions

# def greet_person(name):
#     print(f"Hello, {name}!")

# greet_person("Alice")


# def add_number(a,b):
#     return a + b

# result = add_number(5,3)
# print(result)

#Default Parameters
# def greet_with_title(name, title="Mr."):
#     return f"Hello, {title} {name}!"

# print(greet_with_title("Smith"))
# print(greet_with_title("Johnson", "Dr."))

#Exercise: Write a function to check if a number is prime or not.
# def check_prime(n):
#     # numbers less than or equal to 1 are not prime
#     if n <= 1:
#         return False
    
#     # 2 is the only even prime number
#     if n == 2:
#         return True

#     #exclude all other even numbers
#     if n % 2 == 0:
#         return False

#     #check odd factors up to the square root of n

#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False

#     return True

# #Test
# number = int(input("Enter a number to check if it is prime: "))
# if check_prime(number):
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")

#Exercise 2: Build a temperature converter function. (Celsius to Fahrenheit)
def farh_converter(x):
    f = (x * 9/5) + 32
    return f"{x} degrees Celsius is equal to {f} degrees Fahrenheit."

temp = float(input("Enter a temperature in Celsius:"))

print(farh_converter(temp))

