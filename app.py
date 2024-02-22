def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
select = int(input())
 
number_1 = int(input("first number: "))
number_2 = int(input("second number: "))
 
if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))
 
elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))
elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))

