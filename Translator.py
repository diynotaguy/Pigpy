letters = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiou'

#have some input to determine whether strings also get translated
stringTranslation = True


backslashReplace = '^'
pigpy = f"""
rintpay("ellohay orldway!")
inputway1 = intway(inputay("irstfay umbernay{backslashReplace}n"))
inputway2 = intway(inputay("econdsay umbernay{backslashReplace}n"))
otaltay = inputway1 + inputway2
rintpay(otaltay)
"""
#^pigpy that says hello world!, asks for 2 numbers, spits out the total


def separate(input):
    prevchar = ''
    word = ''
    punctuation = ''
    separated = []
    for char in input:
        if char in letters and len(word)>0:
            word += char
        elif char in letters and len(word)==0 and prevchar != backslashReplace:
            separated.append(punctuation)
            punctuation = ''
            word += char
        elif char not in letters and len(word) != 0:
            separated.append(word)
            word = ''
            punctuation += char
        elif char not in letters:
            punctuation += char
        elif prevchar == backslashReplace:
            punctuation += char
        else:
            print("Else triggered")

        prevchar = char
    return separated


def translateToEnglish(input):
    if input[0] in vowels and input[-3:] == 'way':
        return input[:-3]
    elif input[0] in letters:
        return input[-3:-2] + input[:-3]
    else:
        new = ''
        for char in input:
            if char == backslashReplace:
                new += '\\'
            else:
                new += char
        return new


def main():
    lines = pigpy.readlines()

    for line in lines:
        sequences = separate(line)

        for sequence in sequences:
            if sequence[0] in letters:
                translatedWord = translateToEnglish(sequence)



#with open("translated.py",'w') as translation:
 #   translation.write()

while True:
    pigLatin = input()
    print(pigLatin, '-->', translateToEnglish(pigLatin))