while True:
    try:
        a = int(input('digite um numero:'))
        b = int(input('mais um numero:'))    
        print(a // b)
        print(a / b)

    except:
        print('digite apenas numeros inteiros:')