word = [ "oi" , "rs!" ]
def convertSentence():
    sentence = input("Insira uma frase para traduzir: ").lower()
    translatedSentence = ""

    for char in '?!.,':
        sentence = sentence.replace(char,'')

    listOfWords = sentence.split()
    ...
    
