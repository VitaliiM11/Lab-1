s = str(input("Enter sentence: "))
sentence = s[::-1]
words = sentence.split()
sentence_rev = " ".join(reversed(words))
print("Your reversed sentence: ", sentence_rev)
