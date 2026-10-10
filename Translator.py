from pathlib import Path

letters = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiou'

#have some input to determine whether strings also get translated
stringTranslation = True

pairProbabilities = []


suffix = 'way'

backslashReplace = '^'

"""pigpy = f""""""
rintpay("ellohay orldway!")\n
inputway1 = intway(inputay("irstfay umbernay{backslashReplace}n"))\n
inputway2 = intway(inputay("econdsay umbernay{backslashReplace}n"))\n
otaltay = inputway1 + inputway2\n
rintpay(otaltay)\n
"""


#^pigpy that says hello world!, asks for 2 numbers, spits out the total

#----------------------------------------------------------------------------------------------
# Subroutines:
#----------------------------------------------------------------------------------------------

def separate(input):
    print(f'separate input: {input}')
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

    emptyCount = 0
    for sequ in separated:
        if sequ == '':
            separated.remove(sequ) 
            emptyCount += 1
            #for some reason there's sometimes an empty string at the start of separated
    print(f'Empty sequences removed: {emptyCount}')
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

def main():
    pigpy = open('testProgram.pigpy', 'r')
    lines = pigpy.readlines()
    pigpy.close()
    print('lines read')

    translatedLines = []
    for line in lines:
        sequences = separate(line)
        translatedLine = []
        for sequence in sequences:
            if sequence[0] in letters:
                possibleWords = translateToEnglish(sequence)
                translatedLine.append(possibleWords)
        translatedLines.append(translatedLine)

    print(f'translatedLines: {translatedLines}')

    totalPossibilites = 1
    for l in translatedLines:
        for sequ in l:
            print(f'possibilities for sequ: {sequ}')
            print(len(sequ))
            totalPossibilites = totalPossibilites * (len(sequ) - 1)
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