def fun(x):
    counter=0
    for z in x :
        if z is True: counter+=1
    return counter

var=[True, True, True, False,
     True, False, True, False]

print(fun(var))

