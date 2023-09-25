def recur_fact(x):
    if x == 1:
        return 1
    else:
        return (x * recur_fact(x-1))

print(recur_fact(1))
print(recur_fact(5))

    