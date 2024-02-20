sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
print(sentence.replace("!", " ")) #Prints sentence without the '!'

new_sentence = sentence.replace("!", " ")
print(new_sentence.upper()) #Prints sentence with all capital letters

rev_sentence = new_sentence.upper()
print(rev_sentence[::-1]) #Prints sentence in reverse