def countWords():
    fileName = input("enter file name:")
    openFile = open(fileName, 'r')
    
    numberW = 0
    for line in openFile:
        word = line.split()
        numberW = numberW + len(word)
        print(word)
    print(numberW)   
countWords()
