print("======== CALCULATOR ========")
calc = int(input("Type '1' to start: "))
if calc == 1 :
 a = float(input("Enter first number: "))
 b = float(input("Enter second number: "))
 operation = input("Enter operation: ")
 result = None
 if operation == '+':
    result = a + b
 elif operation == '-':
    result = a - b
 elif    operation == '*':
    result = a*b
 elif operation == '/':
    if b == 0 : print("You can't divide by zero")
    else: result = a/b
 else : print("Error : Unsupported operation")
 if result is not None :
    print("Your result: ", result)
else:
    print("Wrong operation ")