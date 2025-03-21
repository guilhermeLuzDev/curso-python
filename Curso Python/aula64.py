"""
Iterando strings com while
"""
nome = 'Guilherme Carlos' #iteráveis

tamanho_nome = len(nome)
i = 0
new = ''

while i < tamanho_nome:
    letra = nome[i]
    new += f'*{letra}'
    i += 1

new += '*'
print(new)



