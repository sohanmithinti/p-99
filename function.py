def countingWordsFromFile():
    fileName = input("enter the file name: ")
    file1 = open(fileName)    
    file2 = file1.read()
    file3 = file2.split()
    words = len(file3)
    print(words)

countingWordsFromFile()