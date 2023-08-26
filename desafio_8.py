numeros = 236665
lista = [int(digito) for digito in str(numeros)]
maior = max(lista)
lista.remove(maior)
lista_str = ' '.join(map(str, lista))
segundo_maior = max(lista) -1

print(segundo_maior)
print(maior)
