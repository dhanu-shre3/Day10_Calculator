#Calculator

#add
def add(n1, n2):
    return n1 + n2

#subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

#create a if condition with imput that takes
# choice_operators = "Which operation? Choose 1 for addition : +"
# if choice_operators == 1:
#     add
# elif choice_operators == 2:
#     subtract
# elif choice_operators == 3:
#     multiply
# elif choice_operators == 4:
#     divide

#dictionanry with keys = operators and values = functions
operations = {
        "+":add, 
        "-":subtract, 
        "*":multiply,  
        "/":divide }

num1 = int(input("What is your first number?"))
for keys in operations.keys():
    print (keys)

to_continue =  True


while to_continue:
    operator = input("Pick an operation: ")
    num2 = int(input("What is your next number?"))
    calculation_function = operations[operator]
    answer =  calculation_function(num1, num2)
    
    print(f"{num1} {operator} {num2} = {answer}")
    
    if input(f"Type y to continue with {answer} or n to exit: ") == "y":
        num1 = answer
    else:
        to_continue = False

             

    

