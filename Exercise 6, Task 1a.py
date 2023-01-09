def get_int(display_text: str="Input a number between 1-10: "):
    number = input(display_text)
    while number.isdigit() != True: 
        print("Bad input")
        number = input(display_text) 
    number = int(number) 
    return number 

def get_float(display_text: str="Input a number between 1-10: "):
    number = input(display_text)

    while number.isdigit() != True:
        try:
            float(number)
            number = float(number)
            return number
        except:
            print("Bad input")
            number = input(display_text)
    number = float(number)
    return number

newint = get_int() 
newfloat = get_float()
