valor = float(input())
resto = valor
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

print('NOTAS:')

for valores in notas:
    valorInteiro = resto // valores
    resto = resto - valorInteiro * valores
    print('%d nota(s) de R$ %.2f' % (valorInteiro, valores))

print('MOEDAS:')

for valores in moedas:
    valorInteiro = resto // valores
    resto = resto - valorInteiro * valores
    print('%d moeda(s) de R$ %.2f' % (valorInteiro, valores))