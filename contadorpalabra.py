import re

def contador_de_palabras(frase):

    frase = re.sub(r'\W+', ' ', frase)

    listapalabras = frase.split()

    dicc = {}

    for pal in listapalabras:
        if pal in dicc:
            dicc[pal.lower()] += 1
        else:
            dicc[pal.lower()] = 1
    
    return dicc
    
    
