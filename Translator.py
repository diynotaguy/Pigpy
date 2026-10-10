from pathlib import Path

#----------------------------------------------------------------------------------------------

# Notes:
 # backslashes in python must be changed to another escape character (your choice) in pigpy
 # doesn't support """ """ if stringTranslation is disabled
 # doesn't support octal or hex value escape character code

#----------------------------------------------------------------------------------------------

letters = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiou'

englishWords = ['wL1.txt', 'wL2.txt', 'wL3.txt', 'wL4.txt', 'wL5.txt', 'wL6.txt', 'wL7.txt']

#have some input to determine whether strings also get translated
stringTranslation = True

pairProbabilities = []


suffix = 'way'

backslashReplace = '^'

temp = f"""
rintpay("ellohay orldway!")
inputway1 = intway(inputway("irstfay umbernay{backslashReplace}n"))
inputway2 = intway(inputway("econdsay umbernay{backslashReplace}n"))
otaltay = inputway1 + inputway2
rintpay(otaltay)
"""


#^pigpy that says hello world!, asks for 2 numbers, spits out the total

#----------------------------------------------------------------------------------------------
# Subroutines:
#----------------------------------------------------------------------------------------------

def separate(input):
    prevchar = ''
    word = ''
    punctuation = ''
    separated = []
    for char in input:
        if char in letters:
            if len(word) > 0:
                word += char
            elif prevchar == '':
                word += char
            elif len(word) == 0 and prevchar != '\\':
                separated.append(punctuation)
                punctuation = ''
                word += char
            else:
                punctuation += char
        else:
            if len(word) != 0:
                separated.append(word)
                word = ''
                punctuation += char
            else:
                punctuation += char

        prevchar = char
    if len(word) > 0:
        separated.append(word)
    else:
        separated.append(punctuation)

    return separated 

#----------------------------------------------------------------------------------------------

def translateToEnglish(input):
    if input[0] in vowels and input[-3:] == suffix:
        p1 = input[:-3]
        p2 = input[-3:-2] + input[:-3]
        return [p1, p2, 2]
    elif input[0] in letters:
        return [input[-3:-2] + input[:-3], 1]
    else:
        new = ''
        for char in input:
            if char == backslashReplace:
                new += '\\'
            else:
                new += char
        return [new, 1]

#----------------------------------------------------------------------------------------------

def assessPossibilities(lines):
    total = 1
    for l in lines:
        for sequ in l:
            total = total * (len(sequ) - 1)
    return total
    
#----------------------------------------------------------------------------------------------

def verifyWord(word):
    with open('words_alpha.txt' 'r') as words:
        words.readlines()


def main():
    with open('testProgram.pigpy', 'r') as pigpy:
        lines = pigpy.readlines()
    print(f'lines read: {len(lines)}')

    translatedLines = []
    for line in lines:
        sequences = separate(line)
        translatedLine = []
        for sequence in sequences:
            possibleWords = translateToEnglish(sequence)
            translatedLine.append(possibleWords)
        translatedLines.append(translatedLine)

    print(f'translatedLines: {translatedLines}')

    totalPossibilites = assessPossibilities(translatedLines)
    print(f'totalPossibilites: {totalPossibilites}')

    
            
#----------------------------------------------------------------------------------------------
# Calling main:
#----------------------------------------------------------------------------------------------

main()

#with open("translated.py",'w') as translation:
   # translation.write('test\nnewline')


"""
while True:
    pigLatin = input('\n\n')
    print(f'{pigLatin}:')
    list = translateToEnglish(pigLatin)
    if len(list) == 3:
        pairProbabilities.append(list[:2])
    for i in range(list[len(list)-1]):
        print(list[i], end = ' | ')
"""