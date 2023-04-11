def calculator():
        
        num1 = float(input("First num: "))
        num2 = float(input("Second num: "))

        op = input("Choose operation: ")

        if op == "+":
                result = num1 + num2
        elif op == "-":
                result = num1 - num2
        elif op == "*":
                result = num1 * num2
        elif op == "/":
                result = num1 / num2

        print(result)

calculator()