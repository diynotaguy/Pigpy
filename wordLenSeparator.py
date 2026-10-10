#takes a .txt of words on each line and separates them into different .txt files based on word length

namePrefix = 'wL'
docsMade = []
docs = []

with open('testWordLenSeparator.txt', 'r') as original:
    lines = original.readlines()
    for line in lines:
        count = 0
        for i in line:
            count += 1
        docName = namePrefix + str(len(line))
        num = str(count)
        content = f'{line} {num}'
        print(content)
        if len(line) not in docsMade:
            docsMade.append(len(line)) 
            with open(docName, 'x') as newDoc:
                newDoc.write(content.strip())
        else:
            with open(docName, 'a') as doc:
                doc.write(content.strip())

