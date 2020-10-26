def sentence_maker(phrase):
    interrogatives = ("Who", "What", "Why", "When", "How", "Where")
    capitalized = phrase.capitalize()
    if capitalized.startswith(interrogatives):
        return "{}? ".format(capitalized)
    else:
        return "{}. ".format(capitalized)

textstrings = []

while True:
    inputString = input("Say something: ")
    if inputString == "\end":
        break
    else:
        textstrings.append(sentence_maker(inputString))

print("".join(textstrings))

