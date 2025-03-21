"""
Iterável -> str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador
"""
texto = 'Luiz' # iterável
iterador = iter(texto) #iterator

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break

