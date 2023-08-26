n = int(input('digite:'))
if 1 <= n and n <= 150:
    for i in range(1, n +1):
        print(i, end='')
else:
    print('digite um numero entre 1 e 150!!!')