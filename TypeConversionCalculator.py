user_equation = ""
wanted_conversion = ""

def Initialize():
    user_equation = input("Please enter equation to solve: ")
    wanted_conversion = input("Please enter desired output type: ")
    if wanted_conversion == "Hex":
        hex_con()
    if wanted_conversion == "Decimal":
        deci_con()
    if wanted_conversion == "Binary":
        bin_con()

def hex_con():
    print("Hex")

def bin_con():
    print("Binary")

def deci_con():
    print("Decimal")

Initialize()