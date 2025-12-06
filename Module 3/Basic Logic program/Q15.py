name = input("Enter school's name : ")

words = name.split()
abbervation = "".join([word[0].upper() for word in words])

print("Abberviated form : ",abbervation)