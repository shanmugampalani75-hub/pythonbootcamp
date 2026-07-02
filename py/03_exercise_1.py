number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2:"))

while True:
    try:
        result = 0
        Operation = input("Enter operation (+, -, *, /): ")
        
        if Operation == "+":
            result = number1 + number2
            break
        elif Operation == "-":
            result = number1 - number2
            break
        elif Operation == "*":
            result = number1 * number2
            break
        elif Operation == "/":
            if number2 != 0:
                result = number1 / number2
                break
            else:
                print("Cannot divide by zero!")
                Operation = input("Enter operation (+, -, *, /): ")
        else:
            print("Invalid operation! Please enter a valid operation (+, -, *, /).")
            
    except ValueError:
        print("Please enter a valid operation!")

    #Output Validation

print(f"The results of {number1} {Operation} {number2} is: {result}")