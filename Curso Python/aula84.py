"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ['Luiz', 'Maria']
lista_b = lista_a

lista_a[0] = 'Qualquer coisa'
print(lista_b)