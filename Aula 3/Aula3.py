numero = int(input('Digite um numero inteiro: '))

if numero % 2:
    print ('impar')
else:
    print ('par')


frase = input('digite uma frase: ')

lista = frase.split(' ')

for i in range(len(lista)):
    (lista[i])
    len(lista[i])
    print(f'a palavra {lista[i]} tem {len(lista[i])} letras')


senha = input('digite a senha de 4 digitos: ')

senha_correta = "1234"

#primeria opção
while senha != senha_correta:
    senha = input('digite a senha de 4 digitos: ')

print ('esta certo')

#segunda opção
while True:
    if senha == senha_correta:
        break
    senha = input('digite a senha de 4 digitos: ')

print ('esta certo')




n = int(input("Digite um número para calcular o fatorial: "))

fatorial = 1
for i in range(1,n + 1):
    fatorial *= i

print(f'O fatorial de {n} é {fatorial}')




dicionario = {'janeiro':232, 'fevereiro':321, 'junho':589, 'julho':547}

for mes, valor in dicionario.items():
    print (f'{mes}: {valor}')

