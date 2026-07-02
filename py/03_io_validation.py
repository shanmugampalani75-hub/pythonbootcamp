name = str(input("Enter your name: "))
height = float(input("Enter your height: "))

#Input validation
while True: 
    try:
        age = int(input("Enter your age:"))
        if age > 0 and age < 120:
            break
        else:
            print("Age must be a positive number!")
    except ValueError:
        print("Please enter a valid number!")

# Output Validation
print(f"Hello, {name}!")
print(f"You are {age} years old and {height} feet tall.")