"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num_int = input('Digite um número inteiro: ')

try:
    num_int = int(num_int)
    if num_int % 2 == 0:
        print('Par')
    else:
        print('Impar')
except:
    print('Digite um numero inteiro')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora_atual = input('Digite o horário atual: ')

try:
    hora_atual = int(hora_atual)
    if hora_atual <= 11:
        print('Bom dia!')
    elif hora_atual <= 17:
        print('Boa tarde!')
    else:
        hora_atual <= 23
        print('Boa noite')
except:
    print('Digite um número inteiro.')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu primeiro nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:

    if tamanho_nome <= 4:
        print('Seu nome é curto demais.')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
        
else:
    print('Digite um nome.')