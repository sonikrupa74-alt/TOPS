string = input("Enter a sentence: ")
words = string.split()
longest = max(words, key=len)
print(longest)
