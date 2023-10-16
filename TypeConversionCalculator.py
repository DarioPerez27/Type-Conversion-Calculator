import math

equation_arg = ""

def Initialize():
    
    def hex_con():
        print("Hex")

    def bin_con():
        print("Binary")

    def deci_con(deci_equation):
        try:
            initial_result = eval(deci_equation)
            print("Your inital result is:", initial_result)
            print("Your converted result is: PLACEHOLDER")
        except(ZeroDivisionError):
            print("You can't divide by zero")
            
    user_equation = input("Please enter equation to solve: ")
    wanted_conversion = input("Please enter desired output type: ")
    if wanted_conversion == "Hex":
        hex_con()
    if wanted_conversion == "Decimal":
        deci_con(deci_equation=user_equation)
    if wanted_conversion == "Binary":
        bin_con()
    else:
        Initialize()

Initialize()