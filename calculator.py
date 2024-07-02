class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def modulus(self, a, b):
        result = a % b
        self.history.append(f"{a} % {b} = {result}")
        return result

    def exponentiation(self, a, b):
        result = a ** b
        self.history.append(f"{a} ^ {b} = {result}")
        return result

    def integer_divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        result = a // b
        self.history.append(f"{a} // {b} = {result}")
        return result

    

def main():
    calc = Calculator()

    while True:
        print("\nSimple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Exit")
        choice = input("Choose an operation: ")

        if choice in ["1", "2", "3", "4", "5","6"]:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == "1":
                    result = calc.add(num1, num2)
                elif choice == "2":
                    result = calc.subtract(num1, num2)
                elif choice == "3":
                    result = calc.multiply(num1, num2)
                elif choice == "4":
                    result = calc.divide(num1, num2)
                elif choice == "5":
                    result = calc.modulus(num1, num2)
                

                print(f"The result is: {result}")

            except ValueError as ve:
                print(f"Error: {ve}")
            except Exception as e:
                print(f"An error occurred: {e}")

        
        elif choice == "6":
            calc.exit()
        
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
