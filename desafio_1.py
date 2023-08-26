
'''nesse DESAFIO do HACKERRANK, acabei colocando mais validaçoes
'''

while True:
    #TRY para nao quebra quando colocar algum tipo de dados invalido 
    try:
        
        n = int(input('digite um numero:'))
        if n >= 1 and n <= 100 or n == int:
                if (n % 2 == 1) or (n % 2 == 0 and n >= 6 and n <= 20):
                    print('Weird')
                else:
                    print('Not Weird')
        else:
            print('escolha um numero entre 1 e 100!')

    except ValueError:
         print('digite um numero válido.')