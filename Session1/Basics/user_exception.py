class ValueToSmallError(Exception):
    pass 

class ValueToLargeError(Exception):
    pass 

number = 10
while True:
    try: 
       input_num = int(input("Enter number"))
       if  input_num < number:
           raise ValueToSmallError
       elif input_num > number:
           raise ValueToLargeError
       break 
    except ValueToSmallError:
        print("value to small, try again")
    except ValueToLargeError:
        print("value too large , try again")
print("congratulations")
       
       