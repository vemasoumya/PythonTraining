
# Nested function or Inner function
def outer_sum(num1, num2):
    """
     This function
    """
    print ("outer")
    def inner_sum(n1, n2):
        return n1 + n2
    return  inner_sum(num1,num2)

print(outer_sum(10,20))
help(outer_sum)
#print(outer_sum.__doc__)
#help(str())





    
