textSpeakDictionary = {
    "rs"   : "risos" ,
    "tmb"  : "também" ,
    "vc"   :  "você" ,
    "pq"   :  "porque"
}

sentence = input("Insira alguma frse para traduzir corretamente: ").lower()
wordsToTranslate = sentence.split()
translatedSentence = ""

for word in wordsToTranslate:

    if word in textSpeakDictionary:
        translatedSentence += word + " "

print("==>")
print(translatedSentence)
