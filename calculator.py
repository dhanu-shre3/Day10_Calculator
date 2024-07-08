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
num2 = int(input("What is your second number?"))

for keys in operations.keys():
    print (keys)
operator = input("Pick an operation form the line above:")

calculation_function = operations[operator]
answer =  calculation_function(num1, num2)

print(f"{num1} {operator} {num2} = {answer}")
