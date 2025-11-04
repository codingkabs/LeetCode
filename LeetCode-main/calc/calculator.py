numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
signs = ["+", "-", "*", "/"]
#print(signs[0])

# if signs[0] == x:
#     print(True)
    
#input = input("sign")    
signboolean = None
numberone = int(input("Number 1: "))
sign = input("pick sign = + - * /: ")

numbertwo = int(input("Number 2: "))



    
    
if sign in signs:
    if sign == signs[0]:
        print(numberone + numbertwo)
        signboolean = False

    elif sign == signs[1]:
        print(numberone - numbertwo)
        signboolean = False

    elif sign == signs[2]:
        print(numberone * numbertwo)
        signboolean = False

    elif sign == signs[3]:
        print(numberone / numbertwo)
        signboolean = False
    else:
        sign = (input("that was incorrect please pick a sign = + - * /"))







    
#if input == signs[0]:
    
    
