textSpeakDictionary = {
    "rs"   : "risos" ,
    "tmb"   : "também"
}

print("Dicionario = " , textSpeakDictionary )
print("\nrs =" , textSpeakDictionary["rs"])

key = input("nO que você gostaria de converter? : ")
print(key , "=" , textSpeakDictionary[key])
