# ---------------------------------------------documentation ---------------------------------------------

# ------------------------------------------- Python Identifier ------------------------------------------
<!-- Python Identifier 
    :- Name of the class    
    :- Name of the function 
    :- Name of the variable 
    Rule :- 
            :- Alphanumeric characters are allowed.
            :- Underscore ( single (_) means private and double (__) underscore means strongly private).
            :- __main__  if variable or function start and end with double (__) underscore means its a special identifier or language specific identifier (not recomemded).
            :- it should not start with digit.
            :- Case Sensitive programming langurage.
            :- reserve keyword can't be used as identifier.
            :- there is no Max length allowed for identifier.

  
# ------------------------------------------- Reserved words -----------------------------------------------   

In total in python 35 reserved words are there

Reserved Keywords
        False, None, True, and, as, assert, async, await, break, class, 
        continue, def, del, elif, else, except, finally, for, from, global, 
        if, import, in, is, lambda, nonlocal, not, or, pass, raise, 
        return, try, while, with, yield

Note: 
     :- except first there all keywords are in lower case

some descriptions
    async and await:
        async: This keyword is used to define asynchronous functions, which allow you to write non-blocking code.
        await: Used inside an async function to pause execution until the awaited asynchronous operation completes.

    break :
        break is used to exit a loop prematurely, typically within for and while loops.

    del :
        del is used to delete objects or remove elements from a list or dictionary.
    
    global :
        global is used inside a function to indicate that a variable refers to a global variable, not a local one.
    
    lambda :
        lambda is used to create anonymous (nameless) functions, often for short, simple operations.
    
    nonlocal :
        nonlocal is used inside a nested function to indicate that a variable should refer to the nearest enclosing scope that is not global.

    Yield :
        yield is used in generator functions to yield a value one at a time, preserving the function's state.


# ------------------------------------------- Inbuilt Datatype -----------------------------------------------   

Numeric Types:
    int: Represents integers, e.g., 5, -10, 1000.
    float: Represents floating-point numbers (decimals), e.g., 3.14, 0.001, -2.5.

Text Type:
    str: Represents strings (sequences of characters), e.g., "Hello, World!", 'Python', "123".
    
Boolean Type:
    bool: Represents boolean values, True or False.

Sequence Types:

    list: Represents ordered, mutable (changeable) sequences, e.g., [1, 2, 3], ['apple', 'banana', 'cherry'].
    tuple: Represents ordered, immutable (unchangeable) sequences, e.g., (1, 2, 3), ('apple', 'banana', 'cherry').

Set Types:
    set: Represents unordered, mutable collections of unique elements, e.g., {1, 2, 3}, {'apple', 'banana', 'cherry'}.
    frozenset: Represents unordered, immutable collections of unique elements, e.g., frozenset([1, 2, 3]).

Mapping Type:
    dict: Represents unordered collections of key-value pairs, e.g., {'name': 'John', 'age': 30}.

None Type:
    NoneType (None): Represents the absence of a value, often used to indicate the absence of a return value in functions.

Binary Types:
    bytes: Represents a sequence of bytes, e.g., b'Hello'.
    bytearray: Represents a mutable sequence of bytes, e.g., bytearray(b'Hello').

Range Type:
    range: Represents a sequence of numbers, often used in loops, e.g., range(5) generates [0, 1, 2, 3, 4].

Complex Type:
    complex: Represents complex numbers with a real and imaginary part, e.g., 1+2j.

Decimal Type (from the decimal module):
    Represents fixed-point and floating-point arithmetic with arbitrary precision, suitable for financial and decimal calculations.

Datetime Types (from the datetime module):
    datetime: Represents date and time.
    date: Represents a date (year, month, day).
    time: Represents a time of day.
    timedelta: Represents the difference between two dates or times.
    tzinfo: Represents information about time zones.




# ------------------------------------------- Operators in python -----------------------------------------------   
    # :- Arithmatic Operator
    # :- Comparision Operator
    # :- Logical Operator
    # :- Assignment Operator
    # :- Membership Operator
    # :- Identity Operator
    # :- bitwise Operator
    # :- Ternary Operator
    # :- Slice Operator

Note:- In python we have -ve indexes are also present 

Arithmetic Operators:

   a = 10
   b = 5

   +  (Addition):        result_add = a + b     # 10 + 5 = 15
   -  (Subtraction):     result_sub = a - b     # 10 - 5 = 5
   *  (Multiplication):  result_mul = a * b     # 10 * 5 = 50
   /  (Division):        result_div = a / b     # 10 / 5 = 2.0 (float)
   // (Floor Division):  result_floor_div = a // b  # 10 // 5 = 2 (integer)
   %  (Modulus):         result_mod = a % b     # 10 % 5 = 0
   ** (Exponentiation):  result_exp = a ** b     # 10^5 = 100000

Comparison Operators:

   x = 5
   y = 10

   == (Equal to):           is_equal = x == y           # False
   != (Not equal to):       not_equal = x != y           # True
   >  (Greater than):       greater_than = x > y        # False
   <  (Less than):          less_than = x < y           # True
   >= (Greater than or equal to): greater_than_equal = x >= y  # False
   <= (Less than or equal to):    less_than_equal = x <= y     # True

Logical Operators:

   p = True
   q = False

   and (Logical AND):     result_and = p and q  # False
   or  (Logical OR):      result_or = p or q    # True
   not (Logical NOT):     result_not_p = not p  # False

Membership Operator

   my_list = [1, 2, 3, 4, 5]
   my_set = {3, 4, 5, 6, 7}
   my_dict = {'name': 'Alice', 'age': 30}

   # Membership with lists
   is_in_list = 3 in my_list  # True

   # Membership with sets
   is_in_set = 6 in my_set  # True

   # Membership with dictionaries (checks keys)
   is_in_dict = 'name' in my_dict  # True


Assignment Operator

   x = 10  # Assignment

   x += 5  # Addition assignment (x = x + 5)
   x -= 3  # Subtraction assignment (x = x - 3)
   x *= 2  # Multiplication assignment (x = x * 2)
   x /= 4  # Division assignment (x = x / 4)


Bitwise Operators (for integers):

   x = 5  # Binary: 0101
   y = 3  # Binary: 0011

   &  (Bitwise AND):  result_and = x & y  # 0101 & 0011 = 0001 (Decimal: 1)
   |  (Bitwise OR):   result_or = x | y   # 0101 | 0011 = 0111 (Decimal: 7)
   ^  (Bitwise XOR):  result_xor = x ^ y  # 0101 ^ 0011 = 0110 (Decimal: 6)
   ~  (Bitwise NOT):  result_not_x = ~x   # ~0101 = 1010 (Decimal: -6)


Identity Operator

   a = [1, 2, 3]
   b = a  # b references the same list as a

   # Identity (is) - checks if two variables refer to the same object
   is_same_object = a is b  # True

   # Identity (is not) - checks if two variables refer to different objects
   is_different_object = a is not [1, 2, 3]  # True (a and a new list are different objects)

Ternary Conditional Operator

    age = 18
    message = "Adult" if age >= 18 else "Minor"

Slice Operator

    name = 'microsoft'



# ------------------------------------------- Data collection in python -----------------------------------------------
List
    A list is an ordered collection of elements.
    Lists are defined using square brackets 
    Lists allow duplicate elements.
    Lists are mutable.
        Access  :- use indexes
        Add     :-
        Remove  :-
        modify  :- 
