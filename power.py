def powers(a, n, x):
    a = n * x 
    a %= 4

    if a == 1:
        print(2)
    elif a == 2:
        print(4)
    elif a == 3:
        print(8)
    else:
        print(6)

powers(2, 1000000000, 1000000000)