print('''
Programa super secreto
=====================
''')
word = [ "oi" , "rs!" ]
def convertSentence():
    sentence = input("Nome : ").lower()
    sentence = input("Senha : ").lower()
    translatedSentence = "BEM-VINDO PROGRMADOR"

    for char in '?!.,':
        sentence = sentence.replace(char,'')

    listOfWords = sentence.split()
    ...
    
