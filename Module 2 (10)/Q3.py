text = input("Enter text : ")

words = text.split()

unique_words = set(words)

for word in unique_words:
    print(word,":",words.count(word))