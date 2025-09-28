sentence = input("Please write a sentence.\n").split()

lowercase_sentence = [word.lower() for word in sentence] # created a new list for lowercased strings

cleaned_sentence = set(lowercase_sentence)

for word in sorted(cleaned_sentence):
    print(f"{word} : {lowercase_sentence.count(word)}") # this will get the data from its original source and not from the cleaned source
