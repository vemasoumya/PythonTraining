"""lambda function"""

def generate_square():
    """lambda function usage"""
    return lambda x: x * x
new_val = generate_square()
print(new_val(10))


my_list = [2,7,3,5,9]

new_list = list(map(lambda x : x*x , my_list))
print(new_list)
