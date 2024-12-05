import calc

def main():
    
    while True:
        print("Choose an opration: add, sub, mult, div")
        op = input("Enter your operation: ").strip().lower()

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except InvalidInputs:
            print("Error: Please enter valid numbers.")
            continue 

        if op == "add":
            result = calc.add(num1, num2)
        elif op== "sub":
            result = calc.sub(num1, num2)
        elif op == "mult":
            result = calc.mult(num1, num2)
        elif op == "div":
            result = calc.div(num1, num2)
        else:
            print("Error: Unknown operation. Please try again.")
            continue  

        print(f"The result is: {result}")

        new_op = input("\nWould you like to perform another operation? (yes/stop): ").strip().lower()
        if new_op == "stop":
            break 

# Run the main function
if __name__ == "__main__":
    main()
