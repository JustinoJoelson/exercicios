numero_de_alunos = 5
alunos = []

for resultado in range(1, numero_de_alunos + 1):
    nomes = input('Nome do aluno:')
    notas = float(input('Nota do aluno:'))
    alunos.append([nomes, notas])
    
print(alunos)