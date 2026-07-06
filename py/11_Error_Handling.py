#Basic exception handling
# try: 
#     number = int(input("Enter a number: "))
#     result = 10 / number
#     print(result)
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except Exception as e:
#     print(f"An error occurred: {e}")


# using else and finally
# try: 
#     file = open("data.txt", "r")
# except FileNotFoundError:
#     print("File not found!")
# else: 
#     #Executes if not exception occured
#     content = file.read()
#     print("File read successfully")
# finally:
#     #Always executes
#     if 'file' in locals() and not file.closed:
#         file.close()
#         print("File closed")


#Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 120:
        raise ValueError("Age cannot be greater than 120")
    return True

try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")

