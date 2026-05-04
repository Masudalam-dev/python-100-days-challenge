def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

user_num1 = int(input("what's your first number? "))
print(""""Select the Operation: 
+
-
* 
/
""")

user_operation =input("Which operation would you like to do? ")
user_num2 = int(input("What's the other num? "))

if user_operation == "+":
    addition = add(user_num1,user_num2)
    print(addition)
elif user_operation == "-":
    subtract = subtract(user_num1, user_num2)
    print(subtract)
elif user_operation == "*":
    multiply = multiply(user_num1, user_num2)
    print(multiply)
elif user_operation == "/":
    divide = divide(user_num1,user_num2)
    print(divide)
else:
    print("Invalid input!")
