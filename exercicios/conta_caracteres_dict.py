"""
Contagem de caractres em uma frase
Faça:
Frase = : 'banana'
        : 'paralelepipedo'

    >>> 'b: 1'
        'a: 3'
        'n: 2'

    >>> 'p: 3'
        'a: 2'
        'r: 1'
        'l: 2'
        'e: 3'
        'i: 1'
        'd: 1'
        'o: 1'

"""

def contagem_caractere(s):

    contador = {}

    for palavra in s:
        contador[palavra] = contador.get(palavra, 0) + 1
    return contador

if __name__ == '__main__':
    print(contagem_caractere('Carlos'))
    print(contagem_caractere('paralelepipedo'))