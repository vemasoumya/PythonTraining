"""Error Handling"""
X = 42
Y = 0
try:
    print(X / Y)
except ZeroDivisionError as e:
    # Optionally, log e somewhere
    print('Sorry, something went wrong: ', e)
finally:
    print('This always runs on success or failure')
    