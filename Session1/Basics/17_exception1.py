def divide_numbers(num1, num2):   
    return num1/num2 

if (__name__ == '__main__'):
    try:  
        num1 = 1
        num2 = 0      
        if num1 == 1:
            raise Exception("num1 is 1")
        print(divide_numbers(1,0))        
    except ZeroDivisionError as e:    
        print('Sorry, something went wrong: ', e)
    except :    
        print('any other exception')
    finally:
        print('This always runs on success or failure')

