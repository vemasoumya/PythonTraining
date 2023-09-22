"""User defined function"""
def find_min_max(num_list):
    """Function to return multiple values

    Args:
        num_list (list): List of numbers

    Returns:
        tuple: minimum and maximum value
    """
    maximum = num_list[0]
    minimum = num_list[0]
    for num in num_list:
        if num > maximum:
            maximum = num # Replace maximum
    for num in num_list:
        if num < minimum:
            minimum = num # Replace minimum
    return minimum, maximum


#Call findMinMax function
x, y = find_min_max([2,8,5])
print("Min and Max are: ", x , "and" , y)