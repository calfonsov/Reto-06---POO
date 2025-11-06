class PalindromoError(Exception):
    pass

def Palindromo(word: str):
    letters = list()
    for letter in word:
        letters.append(letter)
    new_word = list()
    for letter in range(len(letters) - 1, -1, -1):
        new_word.append(letters[letter])
    if new_word == letters:
        return True
    else:
        raise PalindromoError("La palabra NO es Palíndromo")

try:
    word: str = input("Ingrese una palabra: ")
    print(Palindromo(word))
except PalindromoError as error:
    print(error)
