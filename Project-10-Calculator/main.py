print("Welcome to Calculator App.")

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

store_last_result = 0

while True:

    # First Number
    while True:
        # try - It protects from crash, if user enter wrong input

        try:
            if store_last_result != 0:
                print("Last Calculated value: ", store_last_result)
                user_previous = input("Type 'y' if you wanna use previous value and type 'n' to start with fresh value").lower()
                if user_previous == "y":
                    user_num1 = store_last_result
                    break

            # I have used float here because it handles float and int well. whereas int gets crash for floating values
            user_num1 = float(input("what's your first number? "))
            break
        except:
            print("Invalid Input 😔.")


    print(""""Select the Operation: 
    +
    -
    * 
    /
    """)

    while True:
        user_operation = input("Which operation would you like to do? ")
        if user_operation in ["+","-","*","/"]:
            break
        else:
            print("Please enter Operation(+, -, *, /) value!")

    # Number 2
    while True:
        try:
            user_num2 = float(input("What's the other num? "))
            break
        except:
            print("Enter a valid Num 😢.")

    if user_operation == "+":
        result = add(user_num1,user_num2)

    elif user_operation == "-":
        result = subtract(user_num1, user_num2)

    elif user_operation == "*":
        result = multiply(user_num1, user_num2)

    elif user_operation == "/":
        if user_num2 == 0:
            print("Can't divide by Zero.")
            continue
        result = divide(user_num1,user_num2)

    print(f"Result: {round(result,2)}")
    store_last_result = result

    break






# Second Method
print("Welcome to Calculator App.")


# I have created the function because function work as a block of code which can be used again and again so once i have assign to code. I can use it multiple times
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


num1 = float(input("Enter your first number: "))
print("Choose the operation: + , - , * , / ")
user_operation = input("Enter your calculating operation: ")
# I will use dictionary to store key and values
# keys will be operation and values would be function name
num2 = float(input("Enter your second number: "))
operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print(operation["+"](2, 4))