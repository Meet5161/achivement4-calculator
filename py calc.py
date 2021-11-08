print(" Select an operation to perrform ")
print ("1. ADD")
print ("2. SUBTRACT")
print ("3. MULTIPLICATION")
print ("4. DIVISION \n")

operation = input()

if operation == "1":
    num1 = input("Enter first number= ")
    num2 = input("Enter second number= ")
    print ("The answer is = " + str(int(num1) + int(num2)))

elif operation == "2":
    num1 = input("Enter first number=")
    num2 = input("Enter second number=")
    print ("The answer is = " + str(int(num1) - int(num2)))

elif operation == "3":
    num1 = input("Enter first number=")
    num2 = input("Enter second number=")
    print ("The answer is = " + str(int(num1) * int(num2)))

elif operation == "4":
    num1 = input("Enter first number=")
    num2 = input("Enter second number=")
    print ("The answer is = " + str(int(num1) / int(num2)))

else:
    print("Press 1 to 4")