class AnagramaError(Exception):
    pass

def Anagrama():
    list_word = list(map(str, input("Ingrese palabras: ").split()))

    if len(list_word) < 2:
        raise AnagramaError("Debe ingresar al menos dos palabras.")

    anagram = []
    for i in range(len(list_word)):
        base = sorted(list_word[i])
        grupo = []
        for palabra in list_word:
            if sorted(palabra) == base:
                grupo.append(palabra)
        if len(grupo) > 1 and grupo not in anagram:
            anagram.append(grupo)

    if len(anagram) == 0:
        raise AnagramaError("No se encontraron anagramas.")
    
    return anagram


try:
    print(Anagrama())
except AnagramaError as error:
    print(error)
