frase = 'O Python é uma linguagem de programação multiparadigma Python foi criado por Guido Van Rossum'

i = 0
mais_vezes = 0
letra_mais = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    vezes_letras = frase.count(letra_atual)

    if mais_vezes < vezes_letras:
        mais_vezes = vezes_letras
        letra_mais = letra_atual
    i += 1

    print(letra_atual, vezes_letras)
    

print(f'A letra que apareceu mais vezes foi: "{letra_mais}"{mais_vezes}x')