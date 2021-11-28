def sortedSentence(Sentence):
      
    words = Sentence.split(" ")
      
    words.sort()
      
    newSentence = " ".join(words)
      
    return newSentence  
a = "Keepers calm and carry dethev"
proba= a.lower()
b = (sortedSentence(proba))
c = str.capitalize(b)
print(c)
