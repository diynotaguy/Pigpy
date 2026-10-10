from pathlib import Path
import keyword
import sys

#----------------------------------------------------------------------------------------------

# Notes:
 # backslashes in python must be changed to another escape character (your choice) in pigpy
 # doesn't support """ """ if stringTranslation is disabled
 # doesn't support octal or hex value escape character code

#----------------------------------------------------------------------------------------------

with open('words_alpha.txt', 'r') as temp:
    global engWords
    engWords = set(word.strip() for word in temp)

letters = 'abcdefghijklmnopqrstuvwxyz'
vowels = 'aeiou'

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
            elif len(word) == 0 and prevchar != backslashReplace:
                separated.append(punctuation)
                punctuation = ''
                word += char
            else:
                print('Escape char situation')
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

    if separated[-1:] == '':
        del(separated[-1:])

    return separated 

#----------------------------------------------------------------------------------------------

def translateToEnglish(input):
    if input[0] in vowels and input[-3:] == suffix:
        p1 = input[:-3]
        p2 = input[-3:-2] + input[:-3]
        p1Valid = p1 in engWords or keyword.iskeyword(p1)
        p2Valid = p2 in engWords or keyword.iskeyword(p2)

        if p1Valid and p2Valid:
            return [p1, p2, 2]
        elif p1Valid:
            return [p1, 1]
        elif p2Valid:
            return [p2, 1]
        else:
            print(f'{p1}, {p2} are not in english or python keywords')
            return False
    elif input[0] in letters:
        result = input[-3:-2] + input[:-3]
        resultValid = result in engWords or keyword.iskeyword(result)
        if result in engWords:
            return [result, 1]
        else:
            print(f'{result} is not in english or python keywords')
            return False
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
            #if type(sequ) == 'string':
            total = total * (len(sequ) - 1)
    return total
    
#----------------------------------------------------------------------------------------------

def main():
    with open('testProgram.pigpy', 'r') as pigpy:
        lines = pigpy.readlines()
    print(f'lines read: {len(lines)}')
    translatedLines = []
    lineNum = 0
    for line in lines:
        lineNum += 1
        sequences = separate(line)
        if lineNum == 2:
            print(f'\n\nLine 2 sequences: {sequences}\n\n')
        translatedLine = []
        charNum = 1
        for sequence in sequences:
            charNum += len(sequence)
            possibleWords = translateToEnglish(sequence)

            if type(possibleWords) == bool:
                print(f"Syntax error: error occurred after {translatedLine}\nline num {lineNum} | chars {charNum-len(sequence)}-{charNum-1}", file = sys.stderr)
                print(translatedLine)
                sys.exit(1)
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