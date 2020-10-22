def displayMenu():
    print("trdtr de exprss")
    print("=" * 13)
    print("Menu: ")
    print(" c = converter um frase")
    print(" p = imprimir dicionario")
    print(" a = adicionar uma palavra")
    print(" d = remover uma palavra")
    print(" q = sair")

def convertSentence():
    sentence = input("Insira uma frase para traduzir:").lower()
    translatedSentence = ""

    listOfWords = sentence.split()
    for word in listOfWords:

        if word in textSpeakDictionary:

            translatedSentence += textSpeakDictionary[word] + ' '


        else:
            translatedSentence += word + " "
        print("==>")
        print(translatedSentence)

def addDictionaryItem():
    txtToAdd = input("Insira a expressão a ser adicionada ao dicionario: ")
    meaning = input("O que ela significa?: ")
    textSpeakDictionary[txtToAdd] = meaning

def deleteDictionaryItem():
    txtToDelete = input("Insira a expressão a ser removida ao dicionario: ")
    del textSpeakDictionary[txtToDelete]

textSpeakDictionary = {
    "rs"  : "risos" ,
    "tmb"  : "tambem" ,
    "vc"  : "você" ,
    "pq"  : "porque"
}

runnig = True

displayMenu()

while running == True:

    menuChoice = input(">_").lower()

    if menuChoice == 'c':
        convertSentence()

    elif menuChoice == 'p':
        print(textSpeakDictionary)

    elif menuChoice == 'a':
        addDictionaryItem()

    elif menuChoice == 'd':
        deleteDictionaryItem()

    elif menuChoice == 'q':
        running = False

    else:
        print("Escolha invalida!")
        

            
    