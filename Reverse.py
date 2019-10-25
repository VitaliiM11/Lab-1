s = str(input("Enter text: "))
sentence = s[::-1]
words = sentence.split()
sentence_rev = " ".join(reversed(words))
print(sentence_rev)